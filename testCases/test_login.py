import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
#from utilities.customLogger import LogGen

class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    #logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        # self.logger.info("******* Test_001_Login ********")
        # self.logger.info("******* Verify Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        act_title=self.driver.title
        if act_title=="STech.ai":
            assert True
            self.driver.close()
            # self.logger.info("******* Home Page Title Passed ********")
        else :
            self.driver.save_screenshot(".\\Screenshots\\"+"homePageTitle.png")
            self.driver.close()
            # self.logger.error("******* Home Page Title Failed ******")
            assert False

    def test_login(self,setup):
        # self.logger.info("******* Login Test Started ********")
        # self.logger.info("******* Verify Login Test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp=LoginPage(self.driver)
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.lp.setUsername(username)
        self.lp.setPassword(password)
        self.lp.clickeye()
        self.lp.clickLogin()
        time.sleep(2)
        act_title=self.driver.title
        if act_title=="STech.ai":
            assert True
            self.driver.close()
            # self.logger.info("******* Login Test Passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "login.png")
            self.driver.close()
            # self.logger.error("******* Login Test Failed ********")
            assert False