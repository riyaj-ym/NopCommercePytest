from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, element_type, element_value):
        self.element(element_type, element_value).click()

    def type_in_field(self, element_type, element_value, text):
        self.element(element_type, element_value).send_keys(text)

    def display_status(self, element_type, element_value):
        return self.element(element_type, element_value).is_displayed()

    def enable_status(self, element_type, element_value):
        return self.element(element_type, element_value).is_enabled()

    def move_to_element(self, element_type, element_value):
        action_chain = ActionChains(self.driver)
        ele = self.element(element_type, element_value)
        action_chain.move_to_element(ele).perform()

    def fetch_actual_title(self):
        return self.driver.title

    def element(self, element_type, element_value):
        ele = None
        if element_type.endswith("_xpath"):
            ele = self.driver.find_element(By.XPATH, element_value)
        elif element_type.endswith("_id"):
            ele = self.driver.find_element(By.ID, element_value)
        elif element_type.endswith("_name"):
            ele = self.driver.find_element(By.NAME, element_value)
        elif element_type.endswith("_link_text"):
            ele = self.driver.find_element(By.LINK_TEXT, element_value)
        return ele
