from selenium import webdriver
import time
import math

link_1 = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link_1)
    link_math = (str(math.ceil(math.pow(math.pi, math.e)*10000)))
    print("link_math=",link_math)
    browser.find_element_by_link_text(link_math).click()
    # print(link_answer)
    # browser = webdriver.Chrome()
    # browser.get(link_answer)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city") #firstname, form-group
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    browser_1.quit()

