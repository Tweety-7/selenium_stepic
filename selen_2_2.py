import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
'''
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
'''
link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    n1 = browser.find_element_by_id("num1").text
    n2 = browser.find_element_by_id("num2").text
    sum_1 = int(n1) + int(n2)
    print(sum_1)
    select_table = Select(browser.find_element_by_id("dropdown"))
    select_table.select_by_value(str(sum_1))
    sumbit = browser.find_element_by_class_name('btn.btn-default')
    sumbit.click()
# body > div > form > div > div > button
# /html/body/div/form/div/div/button
finally:
    time.sleep(5)
    browser.quit()

