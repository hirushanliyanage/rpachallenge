import os
import time

import driver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


class RPACHALLENGE:
    def __init__(self):
        os.makedirs("downloads", exist_ok=True)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"download.default_directory": "C:\\Users\\Hiru\\PycharmProjects\\PythonProject\\downloads"})
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://rpachallenge.com/")
        self.file_path = "downloads/challenge.xlsx"
        # Initialize data lists
        self.first_name = []
        self.last_name = []
        self.company_name = []
        self.role_name = []
        self.address = []
        self.email = []
        self.phone_number = []


    def download_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='challenge.xlsx']").click()

    def handle_xlsx(self):
        df = pd.read_excel(self.file_path)
        self.first_name = df["First Name"].values.tolist()
        self.last_name = df["Last Name "].values.tolist()
        self.company_name = df["Company Name"].values.tolist()
        self.role_name = df["Role in Company"].values.tolist()
        self.address = df["Address"].values.tolist()
        self.email = df["Email"].values.tolist()
        self.phone_number = df["Phone Number"].values.tolist()

    def enter_data(self):
        for i in range(0, 10):
            try:
                self.input_data(i)
            finally:
                self.submit_data()

    def submit_data(self):
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.uiColorButton[type='submit']").click()

    def start(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.uiColorButton").click()

    def input_data(self,id):
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]').send_keys(self.first_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelLastName"]').send_keys(self.last_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelCompanyName"]').send_keys(self.company_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelRole"]').send_keys(self.role_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelAddress"]').send_keys(self.address[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelEmail"]').send_keys(self.email[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelPhone"]').send_keys(self.phone_number[id])



    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    rc = RPACHALLENGE()
    time.sleep(2)
    rc.download_file()
    time.sleep(5)
    rc.handle_xlsx()
    rc.start()
    time.sleep(1)
    rc.enter_data()
    time.sleep(5)
    time.sleep(200000)
