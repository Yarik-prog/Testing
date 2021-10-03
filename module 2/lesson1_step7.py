from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
 browser = webdriver.Chrome() 
 browser.get(link)
 time.sleep(1)
 img = browser.find_element_by_id('treasure')
 x = img.get_attribute("valuex")
 y = calc(x)
 input = browser.find_element_by_css_selector('input[id="answer"]')
 input.send_keys(y)
 check_box = browser.find_element_by_css_selector('input[id="robotCheckbox"]')
 check_box.click()
 radio_button = browser.find_element_by_css_selector('input[id="robotsRule"]')
 radio_button.click()
 button = browser.find_element_by_css_selector('.btn')
 button.click()
finally:
 time.sleep(30)
 browser.quit()