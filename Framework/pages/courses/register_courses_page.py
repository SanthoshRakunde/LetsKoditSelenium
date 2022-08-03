import logging
import time

from Framework.utilities import customlogger as cl
from Framework.base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    allCourses_XPATH = "//a[normalize-space()='ALL COURSES']"
    searchCourse_XPATH = "//input[@id='search']"
    clickSearch_XPATH = "//i[@class='fa fa-search']"
    clickCourse_CSS = "img[alt='course image']"
    enrollInCourse_XPATH = "//button[normalize-space()='Enroll in Course']"
    cardNumber_CSS = "input[placeholder='Card Number']"
    expiryDate_NAME = "exp-date"
    cvc_NAME = "cvc"
    buyButton_CSS = "button[class='checkout-button']"

    #Actions
    def clickAllCourses(self):
        self.elementClick(self.allCourses_XPATH, locatorType="xpath")

    def searchCourse(self, coursename):
        self.sendKeys(coursename, self.searchCourse_XPATH, locatorType="xpath")

    def clickSearch(self):
        self.elementClick(self.clickSearch_XPATH, locatorType="xpath")

    def clickCourse(self):
        self.elementClick(self.clickCourse_CSS, locatorType="css")

    def clickenrollInCourse(self):
        self.elementClick(self.enrollInCourse_XPATH, locatorType="xpath")

    def enterCardNumber(self, cardNumber):
        # This frame takes at least 6 seconds to show, it may take more for you
        time.sleep(6)
        # self.switchToFrame(name="__privateStripeFrame8")
        self.SwitchFrameByIndex(self.cardNumber_CSS, locatorType="css")
        self.sendKeysWhenReady(cardNumber, locator=self.cardNumber_CSS, locatorType="css")
        self.switchToDefaultContent()

    def enterExpiryDate(self, expiryDate):
        # self.switchToFrame(name="__privateStripeFrame9")
        self.SwitchFrameByIndex(self.expiryDate_NAME, locatorType="name")
        self.sendKeysWhenReady(expiryDate, locator=self.expiryDate_NAME, locatorType="name")
        self.switchToDefaultContent()

    def enterCvc(self, cvc):
        # self.switchToFrame(name="__privateStripeFrame10")
        self.SwitchFrameByIndex(self.cvc_NAME, locatorType="name")
        self.sendKeysWhenReady(cvc, locator=self.cvc_NAME, locatorType="name")
        self.switchToDefaultContent()

    #Functionality
    def enterCreditCardInformation(self, num, exp, cvc):
        self.enterCardNumber(num)
        self.enterExpiryDate(exp)
        self.enterCvc(cvc)

    def findCourse(self, courseName):
        self.clickAllCourses()
        self.searchCourse(courseName)
        self.clickSearch()

    def enrollCourse(self, num, exp, cvc):
        self.clickenrollInCourse()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvc)
