# import pytest
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://demo.guru99.com/test/newtours/index.php"
    username = "admin"
    password = "1234"

    # verify guest home page
    def test_homePageTitle(self, setup):
     self.driver = setup
     self.driver.maximize_window()
     self.driver.get(self.baseURL)
     self.driver.implicitly_wait(10)

     # verify guest home page title
     act_title = self.driver.title
     if act_title == "Welcome: Mercury Tours":
         self.driver.close()
         assert True
     else:
         self.driver.close()
         assert False


    # test login
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
        # verify member home page title
        if act_title == "Login: Mercury Tours":
            self.driver.close()
            assert True
            print('Member Webpage displayed')
            print('Log In Successful')
        else:
            self.driver.close()  # close chromedriver
            assert False

        # self.lp.clickSignOff()
        # print("Logout Button Clicked")


# To run: pytest -v -s testCases/test_login.py

