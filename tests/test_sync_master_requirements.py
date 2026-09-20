import importlib.util
import tempfile
import unittest
from pathlib import Path

from openpyxl import Workbook


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "sync_master_requirements.py"
SPEC = importlib.util.spec_from_file_location("sync_master_requirements", SCRIPT_PATH)
sync_master_requirements = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(sync_master_requirements)


class SyncMasterRequirementsTests(unittest.TestCase):
    def test_renders_groups_and_escapes_markdown_cells(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workbook_path = Path(temporary_directory) / "master.xlsx"
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Master"
            sheet.append(list(sync_master_requirements.REQUIRED_COLUMNS))
            sheet.append(
                [
                    "R01",
                    "Build first",
                    "The rover shall send a value containing A | B.",
                    "Inspect the signal.",
                    "Choose the radio.",
                    "AB",
                    "To do",
                    "Communications",
                    "Team build choice",
                    "OLD-001",
                ]
            )
            workbook.save(workbook_path)

            rendered = sync_master_requirements.render(workbook_path)

        self.assertIn("## Communications", rendered)
        self.assertIn("A \\| B", rendered)
        self.assertIn("prior IDs: OLD-001", rendered)
        self.assertIn("| R01 | Choose the radio. |", rendered)

    def test_rejects_missing_required_column(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workbook_path = Path(temporary_directory) / "master.xlsx"
            workbook = Workbook()
            workbook.active.title = "Master"
            workbook.active.append(["ID", "Requirement"])
            workbook.save(workbook_path)

            with self.assertRaisesRegex(ValueError, "required header row"):
                sync_master_requirements.render(workbook_path)
