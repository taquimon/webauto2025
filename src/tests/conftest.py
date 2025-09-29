import logging
import pytest
from utils.logger import get_logger

logger = get_logger(__name__)

# Arrange
@pytest.fixture(scope="session")
def first_entry(request):
    env = request.config.getoption("--env")
    logger.debug("Environment: %s", env)
    browser = request.config.getoption("--browser")
    logger.debug("Browser: %s", browser)
    return "a"

# Arrange
@pytest.fixture(scope="class")
def order(first_entry):
    
    return first_entry + "b"


def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='development', help="Environment where the tests are executed"        
    )
    parser.addoption(
        '--browser', action='store', default='chrome', help="Browser to run the web automation tests"
    )

def pytest_configure(config):
    pytest.env = config.getoption("env")
    pytest.browser = config.getoption("browser")