from cleanup import testCleanUp
from database import testDataBase
from previousMonth import testPrevious

def run_pipeline():
    print("starting")
    #testCleanUp()
    testDataBase()
    testPrevious()
    
if __name__ == "__main__":
    run_pipeline()