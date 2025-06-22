## for exception handling purpose

import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()                     ## gets the information about the exception   ### exc_tb is a traceback object that contains information about the exception
    file_name = exc_tb.tb_frame.f_code.co_filename             ## gets the name of the file where the error occurred
    error_message = f"Error occurred in python script named: {file_name} at line number: {exc_tb.tb_lineno} with message: {str(error)}".format(
        file_name=file_name,
        line_number=exc_tb.tb_lineno,
        error_message=str(error)
    )
    return

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)                                                      ## calls the parent class constructor
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  ## gets the error message with details
    
    def __str__(self):
        return self.error_message                               ## returns the error message when the object is printed



### this file will remains the same for all the projects
### this file will be used to handle the exceptions in the project
### just use the try catch block and raise the CustomException with the error message and error detail



# just to check this file: python src/exception.py
# import logging
# if __name__=="__main__":

#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide By Zero Error")
#         raise CustomException(e, sys)