from Pages.BasePage import BasePage


class GetStarted(BasePage):
    my_act_element_xpath = '//span[normalize-space()="My account"]'
    login_ele_xpath = "//span[text()='Log in']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_my_act_element(self):
        self.move_to_element("my_act_element_xpath", self.my_act_element_xpath)

    def click_on_login_element(self):
        self.click_element("login_ele_xpath", self.login_ele_xpath)

    def check_login_element_display_status(self):
        return self.display_status("login_ele_xpath", self.login_ele_xpath)

    def check_login_element_enabled_status(self):
        return self.enable_status("login_ele_xpath", self.login_ele_xpath)
