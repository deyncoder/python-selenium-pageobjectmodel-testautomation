# import pytest
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://demo.guru99.com/test/newtours/index.php"
    username = "admin"
    password = "1234"

    # Validate Guest Home Page
    def test_homePageTitle(self, setup):
     self.driver = setup
     self.driver.maximize_window()
     self.driver.get(self.baseURL)
     self.driver.implicitly_wait(10)

     # validate guest home page title
     act_title = self.driver.title
     if act_title == "Welcome: Mercury Tours":
         assert True
     else:
         assert False

     self.driver.close()

    # Test Login
    def test_login(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        print("Home Page Launched")
        self.lp = LoginPage(self.driver) # create object for LoginPage
        self.lp.setUserName(self.username)
        print("Username Entered")
        self.lp.setPassword(self.password)
        print("Password Entered")
        self.lp.clickSubmit()
        print("Login Button Clicked")
        self.driver.implicitly_wait(10)

        act_title = self. driver.title
        # validate member home page title
        if act_title == "Login: Mercury Tours":
            assert True
        else:
            assert False
        print('Member Webpage displayed')
        print('Log In Successful')
        self.driver.close()

        # self.lp.clickSignOff()
        # print("Logout Button Clicked")


# To run: pytest -v -s testCases/test_login.py

