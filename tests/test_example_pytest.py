"""
Docstring
test_example_pytest.py
Show a demos for pytest tests and fixtures
"""
import logging
import pytest
from utils.logger import get_logger

logger = get_logger(__name__)

class TestExamplePyTest:
    
    """
    Test Example PyTest to show fixtures and tests
    """
    def setup_class(self):
        """
        Setup Class to initialize environment and browser
        """
        logger.debug("Setup class")
        self.environment = pytest.env
        logger.debug("Environment: %s", self.environment)    
        self.browser = pytest.browser
        logger.debug("Browser: %s", self.browser)

    # fixture
    def setup_method(self):
        logger.debug("Setup")


    def test_one(self):
        """
        Test one show the test name
        """
        logger.debug("test one ")

    def test_two(self, first_entry):
        """
        Test two show the test name and a parameter first entry
        @param first_entry: fixture first entry fixture return a string
        @param number: int number return an integer
        @param <name parameter>: <type parameter> <description parameter>
        """
        logger.debug("test two: %s", first_entry)

    def test_three(self, order):
        logger.debug("test three: %s", order)

    # fixture
    def teardown_method(self):
        logger.debug("tearDown")    
    
    def teardown_class(self):
        logger.debug("Teardown class")