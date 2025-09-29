import logging
import unittest

from utils.logger import get_logger

logger = get_logger(__name__, logging.DEBUG)

class TestLogger(unittest.TestCase):
    
    def test_logger(self):
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        
