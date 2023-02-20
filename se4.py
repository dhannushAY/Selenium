from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

class Dhanush():
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
    
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    

    def login(self):
        self.browsing()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()
        
        
    def go_to_pim_module(self):
        pim_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_module.click()

    def edit_employee(self):
        self.wait = WebDriverWait(self.driver, 10)
        edit_button = self.driver.find_element_by_id("edit_button")
        edit_button.click()
        driver = webdriver.Firefox()
        edit_button = driver.find_element(By.ID, "0038")


        editButtonLocator ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/button[2]/i'
        self.driver.find_element(by=By.XPATH, value=self.editButtonLocator).click()
        
        edit_module = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/button[2]/i')
        action = ActionChains(self.driver)
        action.click(on_element=edit_module).perform()

        
    



    def browsing(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def close_browser(self):
        self.driver.quit()

if __name__ == '__main__':
    D = Dhanush()
    D.login()
    D.go_to_pim_module()
    D.edit_employee()
    D.close_browser()
