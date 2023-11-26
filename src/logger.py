import warnings

def custom_warning_function(x):
    if x < 0:
        warnings.warn("This is a custom warning: x is negative", UserWarning)

def process_value(x):
    custom_warning_function(x)
    # Some processing logic here...

# Test the warning
value = -5
process_value(value)

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)











