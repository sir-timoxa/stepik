from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    
    element = browser.find_element_by_css_selector(".form-control.first[required]")
    element.send_keys("x")

    element = browser.find_element_by_css_selector(".form-control.second[required]")
    element.send_keys("x")

    element = browser.find_element_by_css_selector(".form-control.third[required]")
    element.send_keys("x")
    
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


