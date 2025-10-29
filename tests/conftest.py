
import pytest
from selenium import webdriver
import pytest_html

from utilities import ReadConfiguration


@pytest.fixture()
def setUp_and_teardown(request, driver=None):
    browser = ReadConfiguration.read_configuration("Basic Info","browser")
    app_url = ReadConfiguration.read_configuration("Basic Info", "url")
    #app_url1 = ReadConfiguration.read_configuration("Basic Info", "url1")
    #app_url2 = ReadConfiguration.read_configuration("Basic Info", "url2")

    # Initialize the appropriate WebDriver
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Provide a valid browser name: chrome, firefox, or edge")

    driver.maximize_window()
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()