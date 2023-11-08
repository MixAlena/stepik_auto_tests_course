from selenium import webdriver    # Импортируем библиотеку webdriver
from selenium.webdriver import Keys    # Импортируем библиотеку Keys. Для взаимодействия с клавишами клавиатуры (удалить символ, нажать Enter)
from selenium.webdriver.common.by import By    # Импортируем библиотеку By. Для поиска элементов
import time    # Импортируем библиотеку time. Для использования пауз
import datetime    # Импортируем библиотеку datetime. Для отображения даты и времени скриншотов
from selenium.webdriver.common.action_chains import ActionChains    # Импортируем библиотеку ActionChains. Для управления браузером, скроллинга

''' Открываем окно браузера Chrome и переходим по ссылке '''
browser = webdriver.Chrome()    # Открываем браузер Chrome
base_url = 'https://www.saucedemo.com/'    # Задаем имя и значение переменной url (ссылка на сайт)
browser.get(base_url)    # Переходим по ссылке
browser.maximize_window()    # Рсширяем браузер Chrome на весь экран
time.sleep(1)

login_standard_user = 'standard_user'    # Задаем имя и значение переменной логин
password_all = 'secret_sauce'    # Задаем имя и значение переменной пароль

'''Находим поля логин и пароль, вводим их значения'''
# user_name = browser.find_element(By.NAME, 'user-name')    # Поиск поля по NAME
user_name = browser.find_element(By.CSS_SELECTOR, '#user-name')    # Поиск поля по CSS_SELECTOR
user_name.send_keys(login_standard_user)    # Вводим заданный логин
time.sleep(1)

# password = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')    # Поиск поля по placeholder XPATH
password = browser.find_element(By.XPATH, '//input[@id="password"]')    # Поиск поля по ID XPATH
password.send_keys(password_all)    # Вводим заданный пароль
time.sleep(1)

'''Удаление знаков из заполненного поля и очистка поля целиком'''
user_name.send_keys(Keys.BACKSPACE)    # Удаляет последний смивол из поля логин
password.clear()    # Очистка введенного значения целиком из поля пароль
time.sleep(1)

'''Находим кнопку логин'''
# button_login = browser.find_element(By.ID, 'login-button')    # Поиск поля по ID
button_login = browser.find_element(By.XPATH, '//input[@value="Login"]')    # Поиск поля по value XPATH
button_login.click()    # Нажимает на кнопку Login
time.sleep(1)

'''Проверка устойчивости системы при негативных тестах на этапе авторизации'''
warning_text = browser.find_element(By.XPATH, '//h3[@data-test="error"]')    # Поиск поля по параметру тега XPATH
value_warning_text = warning_text.text    # Задаем имя переменной и находим текст ошибки
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'    # Сравниваем значение текста ошибки с требующимся значением
print("Correct")    # Сравнение подтверждает наличие ошибки и не пускает пользователя дальше

'''Перезагрузка страницы и очистка всех полей'''
browser.refresh()
time.sleep(1)

'''Ввод корректных логина и пароля, завершаем авторизацию'''
user_name = browser.find_element(By.CSS_SELECTOR, '#user-name')    # Вводим заданный логин
user_name.send_keys(login_standard_user)
password = browser.find_element(By.XPATH, '//input[@id="password"]')    # Вводим заданный пароль
password.send_keys(password_all)
time.sleep(1)
password.send_keys(Keys.RETURN)    # Завершаем авторизацию без нажатия на кнопку Login

'''Проверка перехода на нужную страницу'''
text_products = browser.find_element(By.XPATH, '//span[@class="title"]')    # Поиск поля по классу тега XPATH
value_text_products = text_products.text    # Задаем значение поля по тексту на странице
print(value_text_products)
assert value_text_products == "Products"    # Сравниваем значение текста на странице с требующимся значением
print("done")

'''Другой вариант проверки перехода на нужную страницу'''
url = 'https://www.saucedemo.com/inventory.html'    # Задаем переменную и значение ссылки перехода на сайт
get_url = browser.current_url    # Задаем имя переменной и присваиваем текущее значение адреса страницы
print(get_url)
assert url == get_url    # Сравниваем значение заданного url с текущим значением страницы
print("Good url")
time.sleep(1)

'''Создание скриншотов на странице'''
# now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')    # Параметры времени для скриншота
# name_screenshot = 'lesson_screenshot_' + now_date + '.png'    # Задаем имя скриншота
# browser.save_screenshot('seleniumLessons//screen//' + name_screenshot)    # Сохраняем скриншот о выполненом задании

'''Взаимодействие с фильтрами на странице'''
filter = browser.find_element(By.XPATH, '//select[@class="product_sort_container"]')    # Поиск и нажатие поля фильтр
filter.click()
time.sleep(1)
filter_menu = browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
filter_menu.click()    # Переход на одно значение вниз
# filter_menu.send_keys(Keys.PAGE_DOWN)    # Переход на одно значение вниз

'''Перемещение по странице по горизонтали(X) и вертикали(Y)'''
# browser.execute_script('window.scrollTo(0, 500)')

'''Скролинг страницы и проверка наличия элемента на странице'''
action = ActionChains(browser)    # Задаем переменную для управления браузером
linkedin_button = browser.find_element(By.XPATH, '//li[@class="social_linkedin"]')    # Находим элемент на странице, к которому нужно переместиться
action.move_to_element(linkedin_button).perform()    # Браузер скролит страницу к нужному элементу

'''Взаимодействие со скрытым меню'''
menu = browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')    # Находим элемент на странице
menu.click()
print("Click burger menu")    # В параметрах кода отображаются новые элементы
time.sleep(1)
link_about = browser.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')    # Находим скрытый элемент на странице
link_about.click()    # Переход на страницу из скрытого меню
print("Click link about")

'''Переход назад и вперед по истории браузера'''
browser.back()
print("Go back page")
time.sleep(3)
browser.forward()
print("Go forward page")

'''Ждем 3 секунды. Закрываем окно браузера'''
time.sleep(3)    # Открываем окно Chrome на 3 сек
browser.quit()    # Закрывает браузер Chrome
