from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Dhanush():
    url = "https://opensource-demo.orangehrmlive.com"
    driver = webdriver.chrome(service=Service(GeckoDriverManager().install()))
    username = "Admin"
    password = "admin123"
    firstname = "Mr"
    lastname = "D"
    employeeId = "999"
    username_locator = "username"
    password_locator = "password"
    loginButtonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    saveButtonLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    

    def login(self):
        self.browsing()
        time.sleep(10)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.loginButtonLocator).click()  
       

    def add_employee(self):
        pim_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_module.click()
        add_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')))
        add_button.click()
        wait = WebDriverWait(self.driver, 10)
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name.send_keys("Mr")
        wait = WebDriverWait(self.driver, 10)
        last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        last_name.send_keys("D")
        wait = WebDriverWait(self.driver, 30)
        EmployeeId = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')))
        save_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')))
        save_button.click()
        
       

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)


D = Dhanush()

D.login()
D.add_employee()