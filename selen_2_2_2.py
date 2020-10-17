"""
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""
import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]').text
    # x = x_element.text
    ok = browser.find_element_by_xpath('//*[@id="answer"]')
    ok.send_keys(calc(x_element))
    #найти кнопки
    check_button = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_button)
    check_button.click()
    radio_button =  browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()
    sumbit = browser.find_element_by_class_name('btn.btn-primary')
    #поскролить вниз execute_script
    browser.execute_script("return arguments[0].scrollIntoView(true);", sumbit)
    #тыкнуть кнопки
    sumbit.click()
finally:
    time.sleep(15)
    browser.quit()

