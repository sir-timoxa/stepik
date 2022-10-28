from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip as pc

browser = webdriver.Firefox()

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    btn1.click()
    alert = browser.switch_to.alert.accept()

    time.sleep(1)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    element = browser.find_element(By.ID, "answer")
    element.send_keys(y)

    sub_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    sub_button.click()

    pc.copy(browser.switch_to.alert.text.split(': ')[-1])
    time.sleep(1)

finally:
    browser.quit()
