import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginTest:
    def loginTest(self):
        baseURL = "https://courses.letskodeit.com/"
        service_obj = Service(r"C:\Users\srakunde\Documents\Coding\BrowswerDrivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.get(baseURL)

        loginLink = driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")
        loginLink.click()

        emailBox = driver.find_element(By.ID, "email")
        emailBox.clear()
        emailBox.send_keys("test@email.com")

        passwordBox = driver.find_element(By.NAME, "password")
        passwordBox.clear()
        passwordBox.send_keys("abcabc")

        signInButton = driver.find_element(By.CSS_SELECTOR, "input[value='Login']")
        signInButton.click()

        userIcon = driver.find_element(By.XPATH, "//img[@class='zl-navbar-rhs-img ']")
        if userIcon is not None:
            print("Login passed")
        else:
            print("Login failed")

        time.sleep(2)
        driver.quit()


chrome = LoginTest()
chrome.loginTest()
