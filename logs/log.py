# logs/log.py

import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, log_filename='application.log'):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = RotatingFileHandler(log_filename, maxBytes=1024*1024*5, backupCount=5)
        
        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

# Example usage:
if __name__ == '__main__':
    # Quick test of the Logger
    logger = Logger('my_log_file.log')
    logger.info('This is an info message.')
    logger.error('This is an error message.')
