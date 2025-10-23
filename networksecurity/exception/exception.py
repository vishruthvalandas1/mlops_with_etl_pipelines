import sys
from networksecurity.logging.logger import logging
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        logging.info(f"Error occured in script:[{self.file_name}] at line number:[{self.line_number}] error message:[{self.error_message}]")
        return f"Error occured in script:[{self.file_name}] at line number:[{self.line_number}] error message:[{self.error_message}]"

if __name__=="__main__":
    try:
        a=1/0
        print("this will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)