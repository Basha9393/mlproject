import sys
from src.logger import logging
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")  # Ignore the custom warning
    # Your code that raises the warning



def error_message_detail(error, error_detail: Exception):
    _, _, exc_tb = error_detail.__traceback__
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: Exception):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



import logging

try:
    # Some code that raises an exception
    x = 1 / 0
except Exception as e:
    custom_exception = CustomException(str(e), e)
    print(custom_exception)
