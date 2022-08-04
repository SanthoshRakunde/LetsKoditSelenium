import time
import unittest

import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestRegisterCourseMultiple(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.order(1)
    #("JavaScript for beginners","1234567893214", "1225", "123"),
    @data(("Selenium WebDriver With Python 3.x","893214", "1024", "321"))
    @unpack
    def test_registerCourseMultiple(self, courseName, ccNum, ccExp, ccCvc):
        self.rc.findCourse(courseName)
        self.rc.clickCourse()
        self.rc.enrollCourse(ccNum, ccExp, ccCvc)
        time.sleep(4)
        self.ts.markFinal("test_invalidEnrollment", True,
                          "Enrollment Failed Verification")





