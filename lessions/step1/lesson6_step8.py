from selenium import webdriver
import time

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("x")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла