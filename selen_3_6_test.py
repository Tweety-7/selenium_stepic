'''
открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте:
'''
import time
import math
import pytest
from selenium import webdriver
import time

answer = math.log(int(time.time()))
link_spis = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]
@pytest.fixture(scope="function")
def bro():
    print("\nstart browser for test..")
    bro = webdriver.Chrome()
    yield bro
    print("\nquit browser..")
    bro.quit()

@pytest.mark.parametrize('linki', link_spis)
def test_num(bro,linki):
    link = f"{linki}"
    bro.implicitly_wait(5)
    bro.get(link)
    ok = bro.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view")
    answer = math.log(int(time.time()))
    ok.send_keys(str(answer))
    btn = bro.find_element_by_class_name('submit-submission')
    btn.click()
    text = bro.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" in text.text, ("НЕТ", text.text)


