import warnings
import sys
from logger import logging  # Assuming logger.py is in the same directory

class MyCustomWarning(UserWarning):
    pass

def check_value(x):
    if x < 0:
        warnings.warn("Value is negative!", MyCustomWarning)

def process_value(x):
    check_value(x)
    # Additional processing logic here...

# Test the warning and exception
value = -5
try:
    process_value(value)
except MyCustomWarning as warning:
    logging.warning("Caught a custom warning: %s", str(warning))
    raise ValueError("Caught a negative value!") from warning

except ValueError as ve:
    logging.error("Caught a value error: %s", str(ve))

except Exception as e:
    logging.error("Caught an unexpected exception: %s", str(e))

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
