import logging
import pytest
from selenium import webdriver
from utils.logger import get_logger
from utils.read_json_data import read_json_file
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy import Actor
from selenium.webdriver.chrome.options import Options as ChromeOptions

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
    # if pytest.browser_type == "chrome":
    #     driver = webdriver.Chrome()
    # elif pytest.browser_type == "firefox":
    #     driver = webdriver.Firefox()
    # elif pytest.browser_type == "edge":
    #     driver = webdriver.Edge()
    # elif pytest.browser_type == "safari":
    #     driver = webdriver.Safari()
    # else:
    #     raise ValueError(f"Browser {pytest.browser_type} is not supported")
    grid_url = "http://localhost:4444/wd/hub"  # Replace with your Hub's address if different

    # Set desired capabilities for the test
    # This specifies that you want to run the test on a Chrome browser
    # You can customize these options based on your Grid's capabilities and testing needs
    options = ChromeOptions()
    #options.browser_version = 'latest'  # Request the latest available Chrome version
    # options.platform_name = 'linux'    # Or 'windows', 'mac' depending on your node OS

    # Create a RemoteWebDriver instance, connecting to the Grid Hub
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # clean up
    yield driver
    
    driver.quit()


@pytest.fixture
def log_test_name(request):
    logger.info("Test name: '%s' started", request.node.name)
    def fin():
        logger.info("Test name: '%s' finished", request.node.name)
    
    request.addfinalizer(fin)

@pytest.fixture()
def actor():
    actor = Actor.named("Edwin").who_can(BrowseTheWeb.using_chrome())
    yield actor
    actor.exit()

@pytest.fixture()
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(params=["link"])
def read_data(request):

    return read_json_file(f"tests/data/{request.param}.json")

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