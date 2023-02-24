from selenium.webdriver.common.action_chains import ActionChains
from libraries.locators import Locators
import allure


# Traditional python Class model
class DragDrop(object):
    def __init__(self, driver, url):
        self.driver = driver
        driver.get(url)

    @allure.step
    def move_a_to_b(self):
        driver = self.driver
        source = driver.find_element_by_id(Locators.id_box_a)
        destination = driver.find_element_by_id(Locators.id_box_b)
        ActionChains(driver).drag_and_drop(source, destination).perform()
