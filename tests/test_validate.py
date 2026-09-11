from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
VALIDATOR = ROOT / "scripts" / "validate.py"


class ValidateRepositoryTests(unittest.TestCase):
    def run_fixture(self, name: str) -> subprocess.CompletedProcess[str]:
        self.assertTrue(VALIDATOR.is_file(), "validator has not been implemented")
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(FIXTURES / name)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_accepts_valid_minimal_skill(self) -> None:
        result = self.run_fixture("valid-minimal")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_rejects_broken_local_resource_link(self) -> None:
        result = self.run_fixture("broken-resource")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("broken local link", result.stdout + result.stderr)

    def test_rejects_skill_frontmatter_without_name(self) -> None:
        result = self.run_fixture("missing-name")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required 'name'", result.stdout + result.stderr)

    def test_rejects_malformed_json_resource(self) -> None:
        result = self.run_fixture("malformed-json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid JSON", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
