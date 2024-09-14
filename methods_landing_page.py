import data
import locators


class CuraHealthLanding:

    def __init__(self, driver):
        self.driver = driver

    # click on make_appointment_button
    def make_appointment_button(self):
        self.driver.find_element(*locators.locators_list.make_appointment_button).click()

