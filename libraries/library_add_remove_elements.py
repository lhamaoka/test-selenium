from libraries.locators import Locators
import allure


@allure.step("Click on add button to create a new button")
def click_on_add_element(driver):
    driver.find_element_by_xpath(Locators.xpath_add_element_button).click()


@allure.step
def count_delete_buttons(driver):
    elements = driver.find_elements_by_xpath(Locators.xpath_delete_button_list)
    return elements


@allure.step
def click_delete_button(driver):
    delete_button = driver.find_element_by_xpath(Locators.xpath_first_delete_button)
    delete_button.click()
