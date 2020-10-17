'''from selenium import webdriver
browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script('document.title="Script executing";')
browser.execute_script("document.title='Script executing';alert('Robots at work');")
'''
from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()
# assert True

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
# / javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);
