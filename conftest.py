from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()