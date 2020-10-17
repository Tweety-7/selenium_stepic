"""
Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""
from selenium import webdriver
import time
import math
link = 'http://suninjuly.github.io/redirect_accept.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    bro = webdriver.Chrome()
    bro.get(link)
    butn = bro.find_element_by_class_name("trollface.btn.btn-primary")
    butn.click()
    first_window = bro.window_handles[0]
    new_window = bro.window_handles[1]
    bro.switch_to.window(new_window)


    # but = bro.find_element_by_class_name("btn.btn-primary")
    # but.click()
    x_el = bro.find_element_by_id("input_value").text
    # print(x_el)
    ok = bro.find_element_by_id("answer")
    ok.send_keys(calc(x_el))
    sumbit = bro.find_element_by_class_name("btn.btn-primary")
    sumbit.click()
    alert = bro.switch_to.alert
    answer = alert.text
    an = answer.split(':')[-1]
    print(an)
    alert.accept()
finally:
    time.sleep(7)
    bro.quit()
