
'''
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
# time.sleep(5) implicitly_wait

button = browser.find_element_by_class_name("btn.btn-primary") #class="btn btn-primary" / Verify
button.click()
# time.sleep(5)
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
# time.sleep(5)
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
browser.quit()
