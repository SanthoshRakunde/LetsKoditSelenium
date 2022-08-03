import pytest
from selenium import webdriver

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class") # <-- note class scope
def oneTimeSetUp(request, browser): # <-- note the additional `request` param
    print("Running one time setUp")
    if browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        print("Running tests on FF")
    else:
        driver = webdriver.Chrome()
        print("Running tests on chrome")

    ## add `driver` attribute to the class under testdemo -->
    if request.cls is not None:
        request.cls.driver = driver
    ## <--

    yield driver
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")