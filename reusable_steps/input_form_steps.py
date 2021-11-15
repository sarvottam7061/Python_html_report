from page_object.AppInputForm import InputForm

import time


def input_step(driver):
    input_form = InputForm(driver, "https://demo.seleniumeasy.com/input-form-demo.html")
    input_form.enter_fname("tester")
    input_form.enter_lname("test")
    input_form.enter_email("Gmail@test.com")
    input_form.enter_phone("8452076438")
    time.sleep(3)
