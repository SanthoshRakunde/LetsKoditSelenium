import logging
from utilities import customlogger as cl
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    signinBtn_XPATH = "//a[normalize-space()='Sign In']"
    emailTextbox_ID = "email"
    passwordTextbox_NAME = "password"
    loginBtn_CSS = "input[value='Login']"

    #Actions
    def ClickSigninBtn(self):
        self.elementClick(self.signinBtn_XPATH, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self.emailTextbox_ID, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self.passwordTextbox_NAME, "name")

    def clickLoginBtn(self):
        self.elementClick(self.loginBtn_CSS, "css")

    #Functionality
    def login(self, email, password):
        self.ClickSigninBtn()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@class='zl-navbar-rhs-img ']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.getText("//span[@class='dynamic-text help-block']", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")
