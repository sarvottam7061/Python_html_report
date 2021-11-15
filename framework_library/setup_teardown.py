from selenium import webdriver


def setup():
    driver = webdriver.Chrome(
        executable_path="C:/Users/843974/PycharmProjects/Python_html_report/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(2)
    return driver


def teardown(driver):
    driver.quit()
