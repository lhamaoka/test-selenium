import pytest
import libraries.library_dynamic_controls as add_remove
import libraries.common as common
from libraries.library_dynamic_controls import EnableDisableTextbox


# Just remove checkbox
@pytest.mark.high_priority
def test_remove_checkbox(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/dynamic_controls"
    common.navigate_url(driver, url)
    add_remove.click_remove_button(driver)
    message = add_remove.verify_text(driver)
    assert message == "It's gone!"
    common.screenshot(driver, "Browser window after assertion")


# Remove and then add button
def test_remove_and_add_checkbox(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/dynamic_controls"
    common.navigate_url(driver, url)
    add_remove.click_remove_button(driver)
    message = add_remove.verify_text(driver)
    assert message == "It's gone!"
    add_remove.click_add_button(driver)
    assert add_remove.verify_checkbox_presence(driver) == True


@pytest.mark.error
@pytest.mark.selenium_error
def test_expected_selenium_error(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/dynamic_controls"
    common.navigate_url(driver, url)
    message = add_remove.verify_text(driver)
    assert message == "It's gone!"


@pytest.mark.error
@pytest.mark.assert_error
def test_expected_assertion_error(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/dynamic_controls"
    common.navigate_url(driver, url)
    add_remove.click_remove_button(driver)
    message = add_remove.verify_text(driver)
    assert message == "Expected error"


@pytest.mark.error
@pytest.mark.python_error
def test_expected_python_error(open_browser):
    driver = open_browser
    driver = driver + 1
    print(driver)


def test_enable_disable_button(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/dynamic_controls"
    class_enable_disable = EnableDisableTextbox(driver, url)
    class_enable_disable.click_enable_button()
    class_enable_disable.click_disable_button()
