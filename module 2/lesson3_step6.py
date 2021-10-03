from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
 browser = webdriver.Chrome() 
 browser.get(link)
 time.sleep(1)

 button = browser.find_element_by_css_selector('.btn')
 button.click()
 time.sleep(1)

 new_window = browser.window_handles[1]
 browser.switch_to.window(new_window)

 value = browser.find_element_by_id("input_value").text
 input = browser.find_element_by_id("answer")
 input.send_keys(calc(int(value)))

 submit = browser.find_element_by_css_selector('.btn')
 submit.click()
finally:
 time.sleep(60)
 browser.quit()