from selenium import webdriver
import time
link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
btn = browser.find_element_by_id("button")
btn.click()
browser.quit()
