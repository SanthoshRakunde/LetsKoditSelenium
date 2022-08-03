import unittest
import pytest
from ddt import ddt, data, unpack
from testdemo.pageclass import PracticePage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):  # <-- note the oneTimeSetup reference here
        self.practice = PracticePage(self.driver)

    def test_methodA(self, text, expectedCount):
        self.driver.get("https://letskodeit.teachable.com/pages/practice")
        #self.driver.find_element_by_id("name").send_keys("test")
        self.practice.enterName(text)
        print("Running method A")

    def test_methodB(self):
        print("Running method B")