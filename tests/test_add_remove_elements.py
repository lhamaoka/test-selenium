import pytest
import allure
import libraries.common as common
import libraries.library_add_remove_elements as add_remove


# Just confirm the functionality works
@allure.title("Test weather we can add a button")
@allure.description("""
Oepn http://the-internet.herokuapp.com/add_remove_elements/

Click on the Add button to add buttons.
""")
@pytest.mark.high_priority
@pytest.mark.sanity_test
def test_add_button(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/add_remove_elements/"
    common.navigate_url(driver, url)
    add_remove.click_on_add_element(driver)
    buttons = add_remove.count_delete_buttons(driver)
    assert len(buttons) == 1


# Create couple of buttons and delete them
@allure.title("Create couple of buttons and delete them")
@pytest.mark.sanity_test
def test_add_two_delete_one(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/add_remove_elements/"
    common.navigate_url(driver, url)

    add_remove.click_on_add_element(driver)
    add_remove.click_on_add_element(driver)
    buttons = add_remove.count_delete_buttons(driver)
    assert len(buttons) == 2
    add_remove.click_delete_button(driver)
    buttons = add_remove.count_delete_buttons(driver)
    assert len(buttons) == 1
