"""
В этом задании в форме регистрации требуется загрузить текстовый файл.
<input type="text" name="lastname" class="form-control" placeholder="Enter last name" required maxlength="32">
Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""

from selenium import webdriver
import time
import os
link = "http://suninjuly.github.io/file_input.html"
cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, '1.txt')
try:
    bro = webdriver.Chrome()
    bro.get(link)
    # text_spis = ["firstname", "lastname", "email"]
    for name in bro.find_elements_by_css_selector(".form-control[required]"):
        name.send_keys("answer")
    bro.find_element_by_id("file").send_keys(file_path)
    bro.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(15)
    bro.quit()

