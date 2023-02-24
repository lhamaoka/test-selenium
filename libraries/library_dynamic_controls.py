from libraries.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


@allure.step("wait until loading complete")
def wait_until_loading_complete(driver):
    spinner = driver.find_element(By.XPATH, Locators.xpath_loading_bar)
    WebDriverWait(driver, 60).until(EC.invisibility_of_element(spinner))


@allure.step
def click_remove_button(driver):
    driver.find_element_by_xpath(Locators.xpath_remove_button).click()
    wait_until_loading_complete(driver)


@allure.step
def click_add_button(driver):
    driver.find_element_by_xpath(Locators.xpath_add_button).click()
    wait_until_loading_complete(driver)


@allure.step
def verify_checkbox_presence(driver):
    presence = driver.find_element_by_xpath(Locators.xpath_checkbox).is_displayed()
    return presence


@allure.step
def verify_text(driver):
    message = driver.find_element_by_xpath(Locators.xpath_id_message).text
    return message


# Traditional python Class model
class EnableDisableTextbox(object):
    def __init__(self, driver, url):
        self.driver = driver
        driver.get(url)

    @allure.step
    def click_enable_button(self):
        self.driver.find_element_by_xpath(Locators.xpath_enable_button).click()

    @allure.step
    def click_disable_button(self):
        self.driver.find_element_by_xpath(Locators.xpath_disable_button).click()