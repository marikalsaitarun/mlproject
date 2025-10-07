import sys
import logging
from datetime import datetime
import os

# ---------------------- Logging Configuration ----------------------
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)  # also prints to console
    ]
)

# ---------------------- Custom Exception ----------------------
def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error information such as file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    """
    Custom Exception class for consistent and detailed error reporting.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


# ---------------------- Example Usage ----------------------
if __name__ == "__main__":
    try:
        a = 1 / 0  # Intentional error
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
