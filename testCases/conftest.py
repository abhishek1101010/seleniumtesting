from datetime import datetime
import os

import pytest
import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser== 'edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("launching Edge browser......")

    elif browser== 'firefox':
        driver=webdriver.Firefox(GeckoDriverManager().install())
        print("launching gecko browser")

    else:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("launching chrome browser")

    return driver

# this will get the value from CLI/hooks in parser variable
def pytest_addoption(parser):
    parser.addoption("--browser")

# this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'abhishek'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+  datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"