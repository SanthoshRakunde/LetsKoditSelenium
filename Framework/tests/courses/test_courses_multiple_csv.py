import time
import unittest
from Framework.utilities.read_csv_data import getCSVData
import pytest
from Framework.pages.courses.register_courses_page import RegisterCoursesPage
from Framework.utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestRegisterCourseMultipleCsv(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.order(1)
    #("JavaScript for beginners","1234567893214", "1225", "123"),
    @data(*getCSVData("C:\\Users\\srakunde\\Documents\\Coding\\Personal\\Python\\Udemy\\LetskodeitpythonProject\\testdata.csv"))
    @unpack
    def test_registerCourseMultiple(self, courseName, ccNum, ccExp, ccCvc):
        self.rc.findCourse(courseName)
        self.rc.clickCourse()
        self.rc.enrollCourse(ccNum, ccExp, ccCvc)
        time.sleep(4)
        self.ts.markFinal("test_invalidEnrollment", True,
                          "Enrollment Failed Verification")





