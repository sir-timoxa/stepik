from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Firefox()

link = 'http://SunInJuly.github.io/execute_script.html'


try:
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    element = browser.find_element_by_css_selector("input#answer")
    element.send_keys(y)
    r_button = browser.find_element_by_css_selector("input#robotCheckbox")
    _ = r_button.location_once_scrolled_into_view
    r_button.click()
    ch_button = browser.find_element_by_css_selector("[for='robotsRule']")
    _ = ch_button.location_once_scrolled_into_view
    ch_button.click()
    sub_button = browser.find_element_by_css_selector(".btn-primary")
    _ = sub_button.location_once_scrolled_into_view
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()
