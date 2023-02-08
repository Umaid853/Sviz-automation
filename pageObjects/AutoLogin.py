import time
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id="name"
    textbox_password_id="password"
    button_eye_xpath= '/html/body/div/div/div[2]/div/div/div[1]/section/div/form/div[2]/div[2]/i'
    button_login_xpath= '/html/body/div/div/div[2]/div/div/div[1]/section/div/form/div[4]/button'
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver


    def setUsername(self,username):
        self.driver.find_element('id',self.textbox_username_id).clear()
        self.driver.find_element('id',self.textbox_username_id).send_keys(username)
        time.sleep(2)

    def setPassword(self,password):
        self.driver.find_element('id',self.textbox_password_id).clear()
        self.driver.find_element('id',self.textbox_password_id).send_keys(password)
        time.sleep(2)

    def clickeye(self):
        self.driver.find_element(By.XPATH, self.button_eye_xpath).click()
        time.sleep(2)

    def clickLogin(self):
        login_form=self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        time.sleep(2)

    def clickLogout(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()