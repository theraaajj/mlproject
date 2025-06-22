## for logging purposes

### to log all the executions happening, (in this one file!!)
## even the execptions being handled
### in order to track the execution.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"             ## this will be the naming convention for the log file, i.e. date and time of execution
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)                      ## this line means, the logs will be stored in the logs folder in the current working directory, i.e. src/logs/2023-10-01_12-00-00.log (or whtevr the name be!!)
os.makedirs(logs_path, exist_ok=True)                                        ## this line will create the logs folder if it does not exist, and will not raise an error if it already exists, just append!!

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)                

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,                                                   ## this will log all the messages with level INFO and above, i.e. INFO, WARNING, ERROR, CRITICAL
)


# to check logger working properly, run in terminal: python src/logger.py
# if __name__=="__main__":
#     logging.info("Logging has been set up successfully.")                   ## this will log the message when the script is run, i.e. when the logger.py file is executed
