import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com')
browser.maximize_window()
time.sleep(1)

user_name = browser.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauce')
time.sleep(1)
password.send_keys(Keys.RETURN)

shop_url = 'https://www.saucedemo.com/inventory.html'
get_url = browser.current_url
assert shop_url == get_url
print("Shop url")
time.sleep(1)

'''Взаимодействие с фильтрами на странице'''
filter = browser.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
filter.click()
time.sleep(1)
filter_menu = browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
filter_menu.click()
# filter.send_keys(Keys.PAGE_DOWN)    # Переход на нижнее значение фильтра (на Маке не сработало, перемащается по странице)
print("Correct")
time.sleep(1)

'''Взаимодействие со скрытым меню'''
menu = browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print("Click burger menu")
time.sleep(1)
link_about = browser.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print("Click link about")

'''Создание скриншотов на странице'''
# now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')    # Параметры времени для скриншота
# name_screenshot = 'critical_path_test_screenshot_' + now_date + '.png'    # Задаем имя скриншота
# browser.save_screenshot('seleniumLessons//screen//' + name_screenshot)    # Сохраняем скриншот о выполненом задании

time.sleep(3)
browser.close()
