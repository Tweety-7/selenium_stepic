import math
from selenium import webdriver
import time
'''
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".'''
'''
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
link = "http://suninjuly.github.io/get_attribute.html"

try:
# открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)
    ''' по 1-ой ссылке
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text'''
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    # print(x)
    y = calc(x)
    # поде для ввода ответа
    ok = browser.find_element_by_xpath('//*[@id="answer"]')
    ok.send_keys(y)
    #
    check_button = browser.find_element_by_id("robotCheckbox")
    radio_button =  browser.find_element_by_id("robotsRule")
    sumbit = browser.find_element_by_class_name('btn.btn-default')
    check_button.click()
    radio_button.click()
    sumbit.click()



finally:
    time.sleep(5)
    browser.quit()


# x = browser.find_element_by_css_selector('[id = "input_value"]').text
# browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))
#
# for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
#     browser.find_element_by_css_selector(selector).click()
#     x_element = browser.find_element_by_id("input_value").text
#     browser.find_element_by_id("answer").send_keys(calc(x_element))
#     elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))
#
#     for elem in elements_to_select:
#         browser.find_element_by_css_selector(elem).click()
#
#     print_answer(browser)
# finally:
#     browser.quit()
# находим элементы текстовое поле, чекбокс, радио-кнопку, кнопку "отправить"
# text_field = con.find_element_by_css_selector("#answer")
# checkbox = con.find_element_by_css_selector("#robotCheckbox")
# radio_btn = con.find_element_by_css_selector("#robotsRule")
# submit_btn = con.find_element_by_css_selector('[type="submit"]')
