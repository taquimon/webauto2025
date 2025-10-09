import logging
import pytest
from selenium import webdriver
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
def driver():
    if pytest.browser_type == "chrome":
        driver = webdriver.Chrome()
    elif pytest.browser_type == "firefox":
        driver = webdriver.Firefox()
    elif pytest.browser_type == "edge":
        driver = webdriver.Edge()
    elif pytest.browser_type == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {pytest.browser_type} is not supported")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # clean up
    yield driver
    
    driver.quit()

@pytest.fixture()
def env(request):
    return request.config.getoption("--env")

def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='development', help="Environment where the tests are executed"        
    )
    parser.addoption(
        '--browser_type', action='store', default='chrome', help="Browser to run the web automation tests"
    )

def pytest_configure(config):
    pytest.env = config.getoption("env")
    pytest.browser_type = config.getoption("browser_type")