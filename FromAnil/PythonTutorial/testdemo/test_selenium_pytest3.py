import pytest
from selenium.webdriver.common.keys import Keys
import logging
#from modulespackage.modules_demo1 import ModulesDemo

#logging.basicConfig(filename="log.txt", level=logging.INFO)

#@pytest.mark.usefixtures("driver", "setUp")

# http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/
class TestClass3:

    def test_one(self, driver, setUp):
        try:
            driver.get("http://www.python.org")
            assert "Python" in driver.title
            elem = driver.find_element_by_name("q")
            elem.send_keys("documentation")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source
        finally:
            logging.info("Test One Video: " + driver.session_id)


    def test_two(self, driver, setUp):
        try:
            driver.get("http://www.google.com")
            elem = driver.find_element_by_name("q")
            elem.send_keys("webdriver")
            elem.send_keys(Keys.RETURN)
        finally:
            logging.info("Test Two Video: " + driver.session_id)