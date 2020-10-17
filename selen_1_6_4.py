from selenium import webdriver
import time

try:
    #тест успешно проходит на: http://suninjuly.github.io/registration1.html
    link = "http://suninjuly.github.io/registration1.html"
    # тест падает на:  http://suninjuly.github.io/registration2.html
    # link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # выбор трёх обязательных полей по цсс-селектору
    name=browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    name_2=browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    mail=browser.find_element_by_css_selector('[placeholder="Input your email"]')
    # заполнение трёх полей
    name.send_keys("name")
    name_2.send_keys("nnn_2")
    mail.send_keys("milo")

    # если найти все обязательные поля - не будет падать на второй ссылке, но мне кажется так красивее =)
    # spis_1 = browser.find_elements_by_css_selector('[required=""]')
    # for s in spis_1:
    #     s.send_keys("answer")

    # Отправляем заполненную форму    inp1 = browser.find_elements_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
