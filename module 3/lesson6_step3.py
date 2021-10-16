import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMain:
 message = ''
 @pytest.mark.parametrize('linkId', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
 def test_send_answer(self, browser, linkId):
     link = f"https://stepik.org/lesson/{linkId}/step/1"
     browser.get(link)
     text_area = browser.find_element_by_css_selector(".ember-text-area ")
     text_area.send_keys(str(math.log(int(time.time()))))
     button = browser.find_element_by_css_selector(".submit-submission")
     button.click()
     result = browser.find_element_by_css_selector(".smart-hints__hint")
     self.message += result.text
     print(self.message)
     assert "Correct!" in result.text