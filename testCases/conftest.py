from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

# def setup(browser):
#     if browser=='chrome':
#       driver=webdriver.Chrome()
#       print("Launching Chrome Browser....")
#     elif browser=='edge':
#         driver = webdriver.Edge()
#         print("Launching Edge Browser....")
#     else:
#         driver=webdriver.Chrome()
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# ##### Pytest HTML Report ########
#
# #It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'ReaDoc'
#     config._metadata['Module Name'] = 'Library'
#     config._metadata['Tester'] = 'Umaid'
#
#
# #It is hook for Delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)