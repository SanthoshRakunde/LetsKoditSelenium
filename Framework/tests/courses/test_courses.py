import time
import pytest
from Framework.pages.courses.register_courses_page import RegisterCoursesPage
from Framework.utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestRegisterCourse:
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.order(1)
    def test_registerCourse(self):
        #self.rc.enrollCourse("JavaScript for beginners", "1234567896", "1225", "123")
        self.rc.findCourse("JavaScript for beginners")
        self.rc.clickCourse()
        self.rc.enrollCourse("1234567893214", "1225", "123")
        time.sleep(4)
        self.ts.markFinal("test_invalidEnrollment", True,
                          "Enrollment Failed Verification")





