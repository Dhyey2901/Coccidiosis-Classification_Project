import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"           #this will save the ascii time log level name module name and message

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")         #Creating a log path
os.makedirs(log_dir,exist_ok=True)      #make the directory

logging.basicConfig(                #creating a final log
    level=logging.INFO,             #logging level
    format= logging_str,            #logging format
    handlers=[                      #logging handlers
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")