import pytest

class PracticePage():

    """
    Page element locators
    """
    _name = "name"

    def __init__(self, driver):
        self.driver = driver


    def enterName(self, name):
        self.driver.find_element_by_id(self._name).send_keys(name)