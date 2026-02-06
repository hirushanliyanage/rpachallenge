import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class RPACHALLENGE:
    """Automates form filling on rpachallenge.com using Selenium WebDriver."""

    def __init__(self) -> None:
        """
        Initialize the RPA Challenge automation.

        Sets up the Chrome WebDriver with custom download directory,
        navigates to the RPA Challenge website, and initializes data lists.
        """
        os.makedirs("downloads", exist_ok=True)
        options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": "C:\\Users\\Hiru\\PycharmProjects\\PythonProject\\downloads"})
        self.driver: WebDriver = webdriver.Chrome(options=options)
        self.driver.get("https://rpachallenge.com/")
        self.file_path: str = "downloads/challenge.xlsx"
        # Initialize data lists
        self.first_name: list[str] = []
        self.last_name: list[str] = []
        self.company_name: list[str] = []
        self.role_name: list[str] = []
        self.address: list[str] = []
        self.email: list[str] = []
        self.phone_number: list[str] = []

    def download_file(self) -> None:
        """
        Download the challenge Excel file from the website.

        Removes any existing file before downloading a fresh copy.

        :return: None
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='challenge.xlsx']").click()

    def handle_xlsx(self) -> None:
        """
        Read the Excel file and populate data lists.

        Parses the downloaded Excel file and extracts data into
        respective instance variables for form filling.

        :return: None
        """
        df: pd.DataFrame = pd.read_excel(self.file_path)
        self.first_name = df["First Name"].values.tolist()
        self.last_name = df["Last Name "].values.tolist()
        self.company_name = df["Company Name"].values.tolist()
        self.role_name = df["Role in Company"].values.tolist()
        self.address = df["Address"].values.tolist()
        self.email = df["Email"].values.tolist()
        self.phone_number = df["Phone Number"].values.tolist()

    def enter_data(self) -> None:
        """
        Loop through all records and fill the form for each.

        Iterates through 10 records, inputs data and submits the form.

        :return: None
        """
        for i in range(0, 10):
            try:
                self.input_data(i)
            finally:
                self.submit_data()

    def submit_data(self) -> None:
        """
        Click the submit button to submit the form.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.uiColorButton[type='submit']").click()

    def start(self) -> None:
        """
        Click the start button to begin the challenge.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "button.uiColorButton").click()

    def input_data(self, id: int) -> None:
        """
        Fill the form fields with data for the given record index.

        :param id: Index of the record in the data lists.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]').send_keys(
            self.first_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelLastName"]').send_keys(
            self.last_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelCompanyName"]').send_keys(
            self.company_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelRole"]').send_keys(self.role_name[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelAddress"]').send_keys(self.address[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelEmail"]').send_keys(self.email[id])
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelPhone"]').send_keys(
            self.phone_number[id])

    def close(self) -> None:
        """
        Close the browser and quit the WebDriver.

        :return: None
        """
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
