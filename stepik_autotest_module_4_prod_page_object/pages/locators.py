from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link1")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form1")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form1")