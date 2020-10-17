from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    # time.sleep(5)
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
