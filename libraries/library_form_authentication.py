from libraries.locators import Locators
import allure


@allure.step
def type_username(driver, username):
    driver.find_element_by_id(Locators.id_username).send_keys(username)


@allure.step
def type_password(driver, password):
    driver.find_element_by_id(Locators.id_password).send_keys(password)


@allure.step
def click_login(driver):
    driver.find_element_by_xpath(Locators.xpath_login_button).click()


@allure.step
def verify_login(driver):
    logged_in = False
    try:
        message = driver.find_element_by_xpath(Locators.xpath_loggedin_message).text
        if "You logged into a secure area!" in message:
            logged_in = True
    except:
        pass
    return logged_in