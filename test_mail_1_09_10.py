import pytest  # Импорт библиотеки pytest
from selenium import webdriver  # Импортируем библиотеку webdriver Для использования пауз
from selenium.webdriver.common.by import By  # Импортируем библиотеку By
import time   # Импорт библиотеки time. Для использования пауз time.sleep(30)
from lesson import driver

@pytest.fixture()
def set_up():
    driver = webdriver.Chrome()  # Открываем браузер Chrome
    driver.get('https://www.saucedemo.com/')  # Переходим через selenium к сайту
    driver.maximize_window()  # Рсширяем браузер Chrome на весь экран
    yield
    time.sleep(5)
    driver.quit()  # Закрывает браузер Chrome

def test_mail_1_09_10(set_up):  #объявление пользовательской функции и
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # Находим поле логина
    user_name.send_keys('standard_user')  # Вводим логин

    password = driver.find_element(By.CSS_SELECTOR, '#password')  # Находим поле пароль
    password.send_keys('secret_sauce')  # Вводим пароль

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')  # Находим кнопку Login
    button_login.click()  # Нажимаем на кнопку

def test_login_2_mail_2(set_up):
    pass
def test_login_3_mail_2(set_up):
    pass
def test_login_4_mail_2(set_up):
    pass

time.sleep(5)