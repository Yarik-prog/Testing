from selenium import webdriver
import os
import math
import time

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file_example.txt")
try:
 browser = webdriver.Chrome() 
 browser.get(link)
 time.sleep(1)

 input1 = browser.find_element_by_css_selector('input[name="firstname"]')
 input1.send_keys('test')

 input2 = browser.find_element_by_css_selector('input[name="lastname"]')
 input2.send_keys('test')

 input3 = browser.find_element_by_css_selector('input[name="email"]')
 input3.send_keys('test')

 element = browser.find_element_by_css_selector("input[type='file']")
 
 element.send_keys(file_path)

 button = browser.find_element_by_css_selector('.btn')
 button.click()

finally:
 time.sleep(30)
 browser.quit()