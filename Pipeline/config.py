from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "Data"

CLEAN_DATA_DIR = DATA_DIR / "CleanData"
UNCLEAN_DATA_DIR = DATA_DIR / "UncleanedData"

# Files move here once they've been processed, so they aren't picked up again
ARCHIVE_RAW_DIR = DATA_DIR / "Archive" / "Raw"
ARCHIVE_LOADED_DIR = DATA_DIR / "Archive" / "Loaded"

# eBird hotspot ID -> display name
LOCATIONS = {
    "L1025768": "FDR",
    "L1069194": "Philadelphia Naval Yard",
    "L1145863": "Wissahickon Valley",
    "L3041917": "Dixon Meadow Preserve",
    "L504403": "John Heinz",
}
