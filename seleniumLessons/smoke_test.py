import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

base_url = 'https://www.saucedemo.com/'
login_standard_user = 'standard_user'
password_all = 'secret_sauce'
shop_url = 'https://www.saucedemo.com/inventory.html'
basket_url = 'https://www.saucedemo.com/cart.html'
information_url = 'https://www.saucedemo.com/checkout-step-one.html'
overview_url = 'https://www.saucedemo.com/checkout-step-two.html'


browser = webdriver.Chrome()
browser.get(base_url)
browser.maximize_window()
time.sleep(1)

user_name = browser.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys(login_standard_user)
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
time.sleep(1)
# button_login = browser.find_element(By.XPATH, '//input[@value="Login"]')
# button_login.click()
password.send_keys(Keys.RETURN)

'''Проверка перехода на нужную страницу'''
get_url = browser.current_url
assert shop_url == get_url
print("Shop url")
time.sleep(1)

'''Скролинг страницы и проверка наличия элемента на странице'''
action = ActionChains(browser)
red_t_shirt = browser.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
action.move_to_element(red_t_shirt).perform()
time.sleep(1)

red_t_shirt.click()
time.sleep(3)

'''Скролинг страницы и проверка наличия элемента на странице'''
basket_button = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
action.move_to_element(basket_button).perform()
time.sleep(1)
basket_button.click()
time.sleep(3)

'''Проверка перехода на нужную страницу'''
get_url = browser.current_url
assert basket_url == get_url
print("Basket url")
time.sleep(1)

checkout_button = browser.find_element(By.XPATH, '//button[@id="checkout"]')
checkout_button.click()
time.sleep(1)

'''Проверка перехода на нужную страницу'''
get_url = browser.current_url
assert information_url == get_url
print("Information url")
time.sleep(1)

first_name = browser.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('qwe')
last_name = browser.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('asd')
postal_code = browser.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.send_keys(123)
time.sleep(1)

'''Очистка введенного значения в поле'''
postal_code.clear()
time.sleep(1)

postal_code.send_keys(123)
time.sleep(1)
continue_button = browser.find_element(By.XPATH, '//input[@id="continue"]').click()

'''Проверка перехода на нужную страницу'''
get_url = browser.current_url
assert overview_url == get_url
print("Overview url")
time.sleep(3)

finish_button = browser.find_element(By.XPATH, '//button[@id="finish"]').click()

'''Проверка перехода на нужную страницу'''
complete_message = browser.find_element(By.XPATH, '//h2[@class="complete-header"]')
value_text_message = complete_message.text    # Задаем значение поля по тексту на странице
print(value_text_message)
assert value_text_message == "Thank you for your order!" 
print("Complete!")
time.sleep(3)

'''Создание скриншотов на странице'''
# now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')    # Параметры времени для скриншота
# name_screenshot = 'smoke_test_screenshot_' + now_date + '.png'    # Задаем имя скриншота
# browser.save_screenshot('seleniumLessons//screen//' + name_screenshot)    # Сохраняем скриншот о выполненом задании

time.sleep(3)
browser.close()
