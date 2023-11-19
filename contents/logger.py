# logger.py
import logging
from datetime import datetime

logging.basicConfig(filename='user_activity_log.log', level=logging.INFO)

def log_activity(action, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"{timestamp} - {action} - {details}")

