from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "Data"

CLEAN_DATA_DIR = DATA_DIR / "CleanData" 
UNCLEAN_DATA_DIR = DATA_DIR / "UncleanedData" 


print(f"{CLEAN_DATA_DIR} and {UNCLEAN_DATA_DIR}")