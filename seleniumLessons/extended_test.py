import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com')
browser.maximize_window()
time.sleep(1)

login_standard_user = 'standard_secret_user'    # Задаем не верное значение логин
password_all = 'secret_sauce'

user_name = browser.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys(login_standard_user)
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
time.sleep(1)
button_login = browser.find_element(By.XPATH, '//input[@value="Login"]')
button_login.click()

'''Проверка устойчивости системы при негативных тестах на этапе авторизации'''
warning_text = browser.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warning_text = warning_text.text
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
print("Correct")

'''Создание скриншотов на странице'''
# now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')    # Параметры времени для скриншота
# name_screenshot = 'extended_test_screenshot_' + now_date + '.png'    # Задаем имя скриншота
# browser.save_screenshot('seleniumLessons//screen//' + name_screenshot)    # Сохраняем скриншот о выполненом задании

'''Перезагрузка страницы и очистка всех полей'''
browser.refresh()


time.sleep(3)
browser.close()
