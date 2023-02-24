class Locators:

    # DRAG AND DROP
    id_box_a = "column-a"
    id_box_b = "column-b"

    # ADD REMOVE BUTTONS
    xpath_add_element_button = "//button[contains(text(),'Add Element')]"
    xpath_delete_button_list = "//div[@id='elements']/button"
    xpath_first_delete_button = "//div[@id='elements']/button[1]"


    # ADD/ REMOVE CHECKBOX
    xpath_remove_button = "//button[contains(text(),'Remove')]"
    xpath_add_button = "//button[contains(text(),'Add')]"
    xpath_loading_bar = "//div[@id='loading']"
    xpath_id_message = "//p[@id='message']"
    xpath_checkbox = "//input[@type='checkbox']"


    # ENABLE / DISABLE BUTTON
    xpath_enable_button = "//button[contains(text(),'Enable')]"
    xpath_disable_button = "//button[contains(text(),'Disable')]"

    # FORM AUTHENTICATION
    id_username = "username"
    id_password = "password"
    xpath_login_button = "//button[@type='submit']"
    xpath_loggedin_message = "//div[@id='flash']"