import time
from selenium.webdriver.common.keys import Keys
import logging

#logging.basicConfig(filename="log.txt", level=logging.INFO)


def test_one(driver, setUp):
    try:
        driver.get("http://www.python.org")
        time.sleep(1)
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("documentation")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    finally:
        logging.info("Test One Video: " + driver.session_id)


def test_two(driver, setUp):
    try:
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("webdriver")
        elem.send_keys(Keys.RETURN)
    finally:
        logging.info("Test Two Video: " + driver.session_id)