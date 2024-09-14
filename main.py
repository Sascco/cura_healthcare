import data
import locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


# Start
class Cura_Tests

    driver = None
    @classmethod
    def Setup(cls):
        chrome_driver_path = r"C:\Users\Sascc\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)

    def test_click_make_appointment_landing
        sleep(3)
        self.driver.get(data.url)





    @classmethod
    def tearDown(cls):
        cls.driver.quit()
