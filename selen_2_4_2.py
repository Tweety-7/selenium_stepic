'''
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод
text_to_be_present_in_element из библиотеки expected_conditions.
'''

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import  time
import math
try:
    bro = webdriver.Chrome()
    bro.get(link)
    # wait = WebDriverWait(bro, 12)
    # price = bro.find_element_by_id("price")
    #Дождаться, когда цена дома уменьшится до $100
    # .text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
    WebDriverWait(bro, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # Нажать на кнопку "Book"
    # button.click()
    book_btn = bro.find_element_by_class_name("btn.btn-primary")
    book_btn.click()
    x_el = bro.find_element_by_id("input_value").text
    ok = bro.find_element_by_id("answer")
    ok.send_keys(calc(x_el))
    sumbit = bro.find_element_by_id("solve")
    sumbit.click()
    alert = bro.switch_to.alert
    answer = alert.text
    an = answer.split(':')[-1]
    print(an)
    alert.accept()
finally:
    time.sleep(95)
    bro.quit()


