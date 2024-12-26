import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[
        logging.FileHandler(filename='logs.log', mode='w'),   # save the log messages as file
        logging.StreamHandler(sys.stdout)                     # display the messages in cmd 
    ]
)