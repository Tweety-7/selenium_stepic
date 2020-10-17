"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""
from selenium import webdriver
import time
import math
link = 'http://suninjuly.github.io/alert_accept.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    bro = webdriver.Chrome()
    bro.get(link)
    # but = bro.switch_to.alert
    # but.accept()
    but = bro.find_element_by_class_name("btn.btn-primary")
    but.click()
    al = bro.switch_to.alert
    al.accept()
    x_el = bro.find_element_by_id("input_value").text
    print(x_el)
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
