from cleanup import testCleanUp
from database import testDataBase
from previousMonth import testPrevious
from historic import testHistory

def run_pipeline():
    print("starting")
    #testCleanUp()
    testDataBase()
    testPrevious()
    testHistory()





    
if __name__ == "__main__":
    run_pipeline()