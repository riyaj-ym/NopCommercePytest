from pytest import mark

from Pages.GetStarted import GetStarted
from utilities import ReadConfigurations


@mark.usefixtures("setup")
class TestLoginPageFunctionality:
    base_url = ReadConfigurations.read_configuration("basic_info", "base_url")

    def test_verify_login_link_on_the_homepage(self, setup):
        driver = setup
        driver.get(self.base_url)
        gs = GetStarted(driver)  # gs=GetStarted page object
        gs.move_to_my_act_element()
        assert gs.check_login_element_display_status() and gs.check_login_element_enabled_status()
        gs.click_on_login_element()
        expected_title = "Login - nopCommerce"
        actual_title = gs.fetch_actual_title()
        assert expected_title == actual_title
