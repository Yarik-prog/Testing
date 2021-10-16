from selenium import webdriver
import time
import unittest


link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
class TestAbs(unittest.TestCase):
 def test_abs1(self):
  browser = webdriver.Chrome()
  browser.get(link2)

  input1 = browser.find_element_by_css_selector('.first_block .first')
  input1.send_keys('test')

  input2 = browser.find_element_by_css_selector('.first_block .second')
  input2.send_keys('test')

  input3 = browser.find_element_by_css_selector('.first_block .third')
  input3.send_keys('test')

  input4 = browser.find_element_by_css_selector('.second_block .first')
  input4.send_keys('test')

  input5 = browser.find_element_by_css_selector('.second_block .second')
  input5.send_keys('test')
 
  button = browser.find_element_by_css_selector("button.btn")
  button.click()
    # находим элемент, содержащий текст
  welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
  welcome_text = welcome_text_elt.text
  self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be welcome text")
        
 def test_abs2(self):
  browser = webdriver.Chrome()
  browser.get(link)

  input1 = browser.find_element_by_css_selector('.first_block .first')
  input1.send_keys('test')

  input2 = browser.find_element_by_css_selector('.first_block .second')
  input2.send_keys('test')

  input3 = browser.find_element_by_css_selector('.first_block .third')
  input3.send_keys('test')

  input4 = browser.find_element_by_css_selector('.second_block .first')
  input4.send_keys('test')

  input5 = browser.find_element_by_css_selector('.second_block .second')
  input5.send_keys('test')
 
  button = browser.find_element_by_css_selector("button.btn")
  button.click()
    # находим элемент, содержащий текст
  welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
  welcome_text = welcome_text_elt.text
  self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be welcome text")

if __name__ == "__main__":
    unittest.main()

