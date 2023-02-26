from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os, sys
from Insurance.utils import get_collection_as_dataframe

# def test_logger_and_exception():
  #  try:
   #     logging.info("Starting the test_logger_and_exception")
   #     result = 3 / 0
   #     print(result)
   #     logging.info("Ending point of the test_logger_and_exception")
    # except Exception as e:
    #    logging.debug(str(e))
     #   raise InsuranceException(e, sys)

if __name__ == "__main__":
    try:
        #start_training_pipeline()
        #test_logger_and_exception() 
        get_collection_as_dataframe(database_name = "INSURANCE", collection_name = 'INSURANCE_PROJECT' )
    except Exception as e:
        print(e)


