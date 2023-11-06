from selenium import webdriver    # Импортируем библиотеку webdriver
from selenium.webdriver import Keys    # Импортируем библиотеку Keys
from selenium.webdriver.common.by import By    # Импортируем библиотеку By
import time    # Импортируем библиотеку time. Для использования пауз

''' Открываем окно браузера Chrome и переходим по ссылке '''
browser = webdriver.Chrome()    # Открываем браузер Chrome
base_url = 'https://www.saucedemo.com/'    # Задаем имя и значение переменной url (ссылка на сайт)
browser.get(base_url)    # Переходим по ссылке
browser.maximize_window()    # Рсширяем браузер Chrome на весь экран
time.sleep(1)

login_standard_user = 'standard_user'    # Задаем имя и значение переменной логин
password_all = 'secret_sauce'    # Задаем имя и значение переменной пароль

'''Находим поле логина и вводим логин'''
# user_name = browser.find_element(By.NAME, 'user-name')    # Поиск поля по NAME
user_name = browser.find_element(By.CSS_SELECTOR, '#user-name')    # Поиск поля по CSS_SELECTOR
user_name.send_keys(login_standard_user)    # Вводим заданный логин
time.sleep(1)

# password = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')    # Поиск поля по placeholder XPATH
password = browser.find_element(By.XPATH, '//input[@id="password"]')    # Поиск поля по ID XPATH
password.send_keys(password_all)    # Вводим заданный пароль
time.sleep(1)

# button_login = browser.find_element(By.ID, 'login-button')    # Поиск поля по ID
button_login = browser.find_element(By.XPATH, '//input[@value="Login"]')    # Поиск поля по value XPATH
button_login.click()    # Нажимает на кнопку Login

'''Проверка перехода на нужную страницу'''
text_products = browser.find_element(By.XPATH, '//span[@class="title"]')    # Поиск поля по тегу XPATH
value_text_products = text_products.text    # Задаем значение поля по тексту на странице
print(value_text_products)
assert value_text_products == "Products"    # Сравниваем значение текста на странице с требующимся значением
print("done")


'''Ждем 3 секунды. Закрываем окно браузера'''
time.sleep(3)    # Открываем окно Chrome на 3 сек
browser.quit()    # Закрывает браузер Chrome
