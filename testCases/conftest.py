import pytest
from selenium import webdriver

def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")