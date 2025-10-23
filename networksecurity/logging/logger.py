import logging
import os
from datetime import datetime

# Log folder
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # ✅ Create logs directory

# Log file name
LOG_File = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
LOG_Path = os.path.join(LOG_DIR, LOG_File)

# Configure logging
logging.basicConfig(
    filename=LOG_Path,
    filemode='w',
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
