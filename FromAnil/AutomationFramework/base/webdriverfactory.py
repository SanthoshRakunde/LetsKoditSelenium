"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as edgeService

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "edge":
            # Set edge driver
            service_obj = edgeService(r"C:\Users\srakunde\Documents\Coding\BrowswerDrivers\msedgedriver.exe")
            driver = webdriver.Edge(service=service_obj)
        elif self.browser == "firefox":
            # Set the FF driver
            service_obj = FFService(r"C:\Users\srakunde\Documents\Coding\BrowswerDrivers\geckodriver.exe")
            driver = webdriver.Firefox(service=service_obj)
        elif self.browser == "chrome":
            # Set chrome driver
            service_obj = chromeService(r"C:\Users\srakunde\Documents\Coding\BrowswerDrivers\chromedriver.exe")
            driver = webdriver.Chrome(service=service_obj)
        else:
            # Set the FF driver
            service_obj = FFService(r"C:\Users\srakunde\Documents\Coding\BrowswerDrivers\geckodriver.exe")
            driver = webdriver.Firefox(service=service_obj)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver