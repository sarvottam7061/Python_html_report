from selenium import webdriver
import sys
from page_object.AppInputForm import InputForm
import time
from reusable_steps.input_form_steps import input_step
# from framework_library.setup_teardown import setup, teardown
sys.path.append("../")

def test_me(selenium_driver):
    # selenium_driver = setup()
    input_step(selenium_driver)
    # teardown(selenium_driver)

# test_me()