import logging
import logging.handlers
import os
from datetime import datetime

def setup_logging_once():
    root_logger = logging.getLogger()
    
    if not root_logger.handlers:
        try:
            log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, f'log_{datetime.now().strftime("%d%m%y_%H%M%S%f")}.log')
            
            print(f"Attempting to write log file at: {log_file}")
            
            file_handler = logging.FileHandler(log_file,encoding='utf-8')
            stream_handler = logging.StreamHandler()
            
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)
            
            root_logger.setLevel(logging.INFO)
            root_logger.addHandler(file_handler)
            root_logger.addHandler(stream_handler)
            
            print("FileHandler and StreamHandler added successfully")

        except Exception as e:
            print(f"Error setting up logging: {e}")
            
def get_logger(name=__name__):
    print(f"get_logger() called for {name}")
    setup_logging_once()
    return logging.getLogger(name)