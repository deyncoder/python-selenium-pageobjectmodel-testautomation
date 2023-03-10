from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_name = "userName"
    textbox_password_name = "password"
    button_submit_xpath = "//*[@name='submit']"
    # link_signoff_xpath = "//a[contains(text(),'SIGN-OFF')]"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Enter Username
    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    # Enter Password
    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    # Click Submit
    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    # Click Sign Off
    # def clickSignOff(self):
    #     self.driver.find_element(By.XPATH, self.link_signoff_xpath).click()