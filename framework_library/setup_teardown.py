from selenium import webdriver


def setup():
    driver = webdriver.Chrome(
        executable_path="/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(2)
    return driver


def teardown(driver):
    driver.quit()
