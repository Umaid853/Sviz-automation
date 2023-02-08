import time
import pytest
from selenium import webdriver
from pageObjects.AutoLogin import LoginPage

class Test_001_Login:
    baseURL = "http://10.0.0.118/login"
    username = "superadmin"
    password = "admin123"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        act_title=self.driver.title
        if act_title=="STech.ai":
            assert True
            self.driver.close()
        else :
            self.driver.save_screenshot(".\\Screenshots\\" + "homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickeye()
        self.lp.clickLogin()
        time.sleep(2)
        act_title=self.driver.title
        if act_title=="STech.ai":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "login.png")
            self.driver.close()
            assert False