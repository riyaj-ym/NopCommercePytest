import time
import allure
import pytest
from allure_commons.types import AttachmentType
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@fixture()
def log_on_failure(request):
    # logger = LogGen.log_gen()
    yield
    item = request.node
    if item.rep_call.failed:
        # logger.info("*************** Failed *************** ")
        test_name = item.nodeid
        # driver.save_screenshot("./screenshots/" + str(test_name) + ".png")
        allure.attach(driver.get_screenshot_as_png(), name=test_name,
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@fixture()
def setup(request):
    global driver
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("detach", True)
    ops.add_argument("--start-maximized")
    ops.add_argument("--disable-notifications")
    ser_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=ser_obj, options=ops)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(3)
    driver.close()
