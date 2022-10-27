from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Firefox()

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser.get(link)

    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    z = int(x) + int(y)
    k = Select(browser.find_element(By.ID, "dropdown"))
    k.select_by_value(str(z))

    sub_button = browser.find_element_by_css_selector(".btn-default")
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()
