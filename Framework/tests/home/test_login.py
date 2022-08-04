import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogin:
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.order(2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.order(1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "invalid")
        print(self.lp.verifyLoginFailed())
        assert "Your username or password is invalid. Please try again." == self.lp.verifyLoginFailed()
