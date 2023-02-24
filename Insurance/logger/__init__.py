import logging
from datetime import datetime
import os

# Creating logs directory to store log in files
LOG_DIR = "Insurance_log"

# Creating file name for log file based on current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Here, We are going to define the path to store log with folder_name
LOG_FIlE_NAME = f"log_{CURRENT_TIME_STAMP}.log"


#Creating LOG_DIR if it does not exists.
os.makedirs(LOG_DIR, exist_ok=True)

#Creating file path for projects.
LOG_FIlE_PATH = os.path.join(LOG_DIR, LOG_FIlE_NAME)

# If you want to read log select baseconfig and press f12 from your system.
logging.basicConfig(filename=LOG_FIlE_PATH,
filemode = "w",
format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
#level=logging.INFO,
level=logging.DEBUG,
)
