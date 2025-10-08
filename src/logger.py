import logging
import os
from datetime import datetime
import sys

# ---------------------- Logging Configuration ----------------------

# Create a folder named 'logs' (only directory, not with log filename)
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),   # write to file
        logging.StreamHandler(sys.stdout)     # print to console
    ]
)

if __name__ == "__main__":
    logging.info("Logging has started")
