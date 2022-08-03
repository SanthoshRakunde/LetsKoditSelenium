import unittest
import pytest

@pytest.mark.usefixtures("driver")
class TestClass1(unittest.TestCase):

    # def setUpClass(cls):
    #     print("*#" * 30)
    #     print("Class 1 -> class level setUp")
    #     print("*#" * 30)

    def setUp(self):
        print("Class 1 -> setUp")

    def test_class1_methodA(self):
        self.driver.get("https://letskodeit.teachable.com/pages/practice")
        self.driver.find_element_by_id("name")
        print("Running class 1 -> method A")

    def test_class1_methodB(self):
        print("Running class 1 -> method B")

    def tearDown(self):
        print("Class 1 -> tearDown")

    # def tearDownClass(cls):
    #     print("*#" * 30)
    #     print("Class 1 -> class level tearDown")
    #     print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)