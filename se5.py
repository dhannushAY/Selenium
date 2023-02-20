from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OrangeHRM:
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
    
    def edit_employee(self):
        pim_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_module.click()

        first_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName")))
        first_name.send_keys("Alice")
        wait = WebDriverWait(self.driver, 10)
        last_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "lastName")))
        last_name.send_keys("Duval")
        wait = WebDriverWait(self.driver, 10)
        search_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
        search_button.click()
        EmployeeId = self.driver.find_element_by_id("0221")
        EmployeeId = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '///*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[1]')))
        
        delete_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[50]/div/div/div[1]/div[2]/div/div/button[1]/i')))
        delete_button.click()
       
       
        
    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


O = OrangeHRM()

O.login()
O.edit_employee()

