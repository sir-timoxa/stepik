from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Firefox()

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(link)

    x_element = browser.find_element_by_css_selector("img#treasure")
    x = x_element.get_attribute('valuex')
    y = calc(x)
    element = browser.find_element_by_css_selector("input#answer")
    element.send_keys(y)
    r_button = browser.find_element_by_css_selector("input#robotCheckbox")
    r_button.click()
    ch_button = browser.find_element_by_css_selector("[id='robotsRule']")
    ch_button.click()
    sub_button = browser.find_element_by_css_selector(".btn-default")
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()
