from selenium import webdriver
import math
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


browser = webdriver.Firefox()

link = "http://suninjuly.github.io/file_input.html"


try:
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk@mail.ru")

    input_file = browser.find_element_by_name("file")
    input_file.send_keys(file_path)

    sub_button = browser.find_element_by_css_selector(".btn-primary")
    _ = sub_button.location_once_scrolled_into_view
    sub_button.click()
finally:
    time.sleep(5)
    browser.quit()
