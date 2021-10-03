from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
 browser = webdriver.Chrome() 
 browser.get(link)
 time.sleep(1)
 x_element = browser.find_element_by_css_selector('span[id="input_value"]')
 x = x_element.text
 y = calc(x)
 input = browser.find_element_by_css_selector('input[id="answer"]')
 input.send_keys(y)
 check_box = browser.find_element_by_css_selector('[for="robotCheckbox"]')
 check_box.click()
 radio_button = browser.find_element_by_css_selector('[for="robotsRule"]')
 radio_button.click()
 button = browser.find_element_by_tag_name("button")
 button.click()
finally:
 time.sleep(30)
 browser.quit()