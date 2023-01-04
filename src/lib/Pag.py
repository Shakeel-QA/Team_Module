from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select


class HomePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(HomePage):
    url = "https://staging.brandsignals.io/campaign//"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)

    def enter_username(self, xpath: str, username: str):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, xpath).send_keys(username)

    def enter_password(self, xpath: str, password: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(password)

    def submit_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()


class Click(HomePage):
    def Click_button(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()


class SendKeys(HomePage):
    def send_keys(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)


from selenium.webdriver.support.ui import Select
import random


def get_selection_list(driver, xpath):
    select_options = driver.find_elements(By.XPATH, f"{xpath}/option")
    options = []
    # getting option
    for option in select_options:
        options.append(option.get_attribute("value"))
    rand_option = random.choice(options[1:])
    # selection
    select = Select(driver.find_element(By.XPATH, xpath))
    select.select_by_value(rand_option)
    return rand_option
