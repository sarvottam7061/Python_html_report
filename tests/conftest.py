from selenium import webdriver
import pytest
import sys
sys.path.append("../")
@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome(
        executable_path="../drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()