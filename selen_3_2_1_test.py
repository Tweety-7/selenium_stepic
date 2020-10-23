import unittest
from selenium import webdriver
import time

'''class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()'''

'''

'''

def register(link, selectors, btn_css):

    bro = webdriver.Chrome()
    bro.get(link)
    for selector in selectors:
        name = bro.find_element_by_css_selector(selector)
        name.send_keys("answer")
    btn = bro.find_element_by_css_selector(btn_css)
    btn.click()
    time.sleep(3)
    welcome_text_elt = bro.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    bro.quit()
    return welcome_text


class TestAssert(unittest.TestCase):
    def test_registered_1(self):
            link = "http://suninjuly.github.io/registration1.html"
            welcome_text = register(link, ['[placeholder="Input your first name"]', '[placeholder="Input your last name"]',
                                           '[placeholder="Input your email"]'],
                                    "button.btn")

            # name= bro.find_element_by_css_selector('[placeholder="Input your first name"]')
            # name_2= bro.find_element_by_css_selector('[placeholder="Input your last name"]')
            # mail= bro.find_element_by_css_selector('[placeholder="Input your email"]')
            # name.send_keys("name")
            # name_2.send_keys("nnn_2")
            # mail.send_keys("milo")
            # time.sleep(3)
            # button = bro.find_element_by_css_selector("button.btn")
            # button.click()
            # time.sleep(5)
            # welcome_text_elt = bro.find_element_by_tag_name("h1")
            # welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "must be text")


    def test_registered_2(self):
        # try:
            link = " http://suninjuly.github.io/registration2.html"
            welcome_text = register(link, ['[placeholder="Input your first name"]', '[placeholder="Input your last name"]',
                                           '[placeholder="Input your email"]'],
                                    "button.btn")
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "must be text")

        # finally:
        #     time.sleep(5)
        #     bro.quit()


if __name__ == "__main__":
    unittest.main()
