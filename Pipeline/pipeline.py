from cleanup import clean_all_files
from database import getCsvFiles
from config import CLEAN_DATA_DIR



def run_pipeline():
    # Clean everything in UncleanedData, then load CleanData into PostgreSQL
    clean_all_files()
    getCsvFiles(CLEAN_DATA_DIR)



if __name__ == "__main__":
    run_pipeline()
