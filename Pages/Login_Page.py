from selenium.webdriver.common.by import By

from helper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):
    usernameTxt = (By.ID, "user-name")
    passwordTxt = (By.ID, "password")
    loginButton = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.webelement_enter(self.usernameTxt, username)
        self.webelement_enter(self.passwordTxt, password)
        self.webelement_click(self.loginButton)
