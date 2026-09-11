#!/usr/bin/env python3
"""Validate the portable structure of a MomentySkills checkout."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
URL_SCHEME_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
IGNORED_PARTS = {".git", ".venv", "__pycache__"}


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return None


def repository_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        # The intentionally invalid fixtures validate failure behavior and are
        # checked individually by the unit tests.
        if relative.parts[:2] == ("tests", "fixtures"):
            continue
        files.append(path)
    return files


def validate_yaml_files(root: Path, errors: list[str]) -> None:
    for path in repository_files(root):
        if path.suffix.lower() in {".yaml", ".yml"}:
            load_yaml(path, errors)


def validate_json_files(root: Path, errors: list[str]) -> None:
    for path in repository_files(root):
        if path.suffix.lower() != ".json":
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: invalid JSON: {exc}")


def skill_frontmatter(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read SKILL.md: {exc}")
        return None

    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter")
        return None

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid frontmatter YAML: {exc}")
        return None

    if not isinstance(frontmatter, dict):
        errors.append(f"{path}: frontmatter must be a mapping")
        return None

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{path}: missing required 'name' in frontmatter")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append(f"{path}: skill name '{name}' must use lowercase letters, digits, and hyphens")
    elif len(name) > 64:
        errors.append(f"{path}: skill name must be at most 64 characters")
    elif name != path.parent.name:
        errors.append(f"{path}: skill name '{name}' does not match directory '{path.parent.name}'")

    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path}: missing required 'description' in frontmatter")
    elif len(description) > 1024:
        errors.append(f"{path}: skill description must be at most 1024 characters")

    return frontmatter


def safe_relative_path(root: Path, value: str) -> Path | None:
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        return None
    return resolved


def validate_metadata(root: Path, errors: list[str]) -> None:
    path = root / "metadata.yaml"
    if not path.is_file():
        errors.append(f"{path}: repository metadata is required")
        return

    data = load_yaml(path, errors)
    if not isinstance(data, dict):
        errors.append(f"{path}: metadata must be a mapping")
        return

    if data.get("schema_version") != 1:
        errors.append(f"{path}: schema_version must be 1")

    project = data.get("project")
    if not isinstance(project, dict):
        errors.append(f"{path}: project must be a mapping")
    else:
        for key in ("name", "repository", "status", "license"):
            if not isinstance(project.get(key), str) or not project[key].strip():
                errors.append(f"{path}: project.{key} must be a non-empty string")

    entries = data.get("skills")
    if not isinstance(entries, list) or not entries:
        errors.append(f"{path}: skills must be a non-empty list")
        return

    listed_names: set[str] = set()
    listed_paths: set[Path] = set()
    for index, entry in enumerate(entries):
        label = f"{path}: skills[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be a mapping")
            continue
        name = entry.get("name")
        relative_path = entry.get("path")
        status = entry.get("status")
        if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{label}.name must be a lowercase hyphenated skill name")
            continue
        if name in listed_names:
            errors.append(f"{label}.name duplicates '{name}'")
        listed_names.add(name)
        if not isinstance(status, str) or not status.strip():
            errors.append(f"{label}.status must be a non-empty string")
        if not isinstance(relative_path, str):
            errors.append(f"{label}.path must be a string")
            continue
        skill_dir = safe_relative_path(root, relative_path)
        if skill_dir is None:
            errors.append(f"{label}.path must stay inside the repository")
            continue
        listed_paths.add(skill_dir)
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{label}.path does not contain SKILL.md")
            continue
        frontmatter = skill_frontmatter(skill_file, errors)
        if frontmatter is not None and frontmatter.get("name") != name:
            errors.append(f"{label}.name does not match {skill_file} frontmatter")

    skills_root = root / "skills"
    discovered = {
        child.resolve()
        for child in skills_root.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    } if skills_root.is_dir() else set()
    for unlisted in sorted(discovered - listed_paths):
        errors.append(f"{unlisted}: skill is not listed in metadata.yaml")


def link_destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        value = value[1:value.index(">")]
    else:
        value = value.split(maxsplit=1)[0]
    return unquote(value.split("#", 1)[0].split("?", 1)[0])


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    for path in repository_files(root):
        if path.suffix.lower() != ".md":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read Markdown: {exc}")
            continue
        for match in MARKDOWN_LINK_PATTERN.finditer(content):
            raw = match.group(1).strip()
            if not raw:
                continue
            destination = link_destination(raw)
            if (
                not destination
                or destination.startswith(("#", "//"))
                or URL_SCHEME_PATTERN.match(destination)
            ):
                continue
            if destination.startswith("/"):
                errors.append(f"{path}: non-portable absolute local link '{raw}'")
                continue
            resolved = (path.parent / destination).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{path}: local link escapes repository '{raw}'")
                continue
            if not resolved.exists():
                errors.append(f"{path}: broken local link '{raw}'")


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"{root}: repository directory does not exist"]
    validate_yaml_files(root, errors)
    validate_json_files(root, errors)
    validate_metadata(root, errors)
    validate_markdown_links(root, errors)
    return sorted(set(errors))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    return parser.parse_args()


def main() -> int:
    if sys.version_info < (3, 11):
        print("Validation requires Python 3.11 or newer.", file=sys.stderr)
        return 2
    root = parse_args().root.resolve()
    errors = validate_repository(root)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
