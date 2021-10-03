from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
 browser = webdriver.Chrome() 
 browser.get(link)
 time.sleep(1)

 x = browser.find_element_by_id('input_value').text
 y = calc(int(x))

 input = browser.find_element_by_css_selector('input[id="answer"]')
 input.send_keys(y)

 button = browser.find_element_by_css_selector('.btn')
 browser.execute_script("return arguments[0].scrollIntoView(true);", button)

 check_box = browser.find_element_by_css_selector('input[id="robotCheckbox"]')
 check_box.click()

 radio_button = browser.find_element_by_css_selector('input[id="robotsRule"]')
 radio_button.click()

 button.click()
finally:
 time.sleep(30)
 browser.quit()