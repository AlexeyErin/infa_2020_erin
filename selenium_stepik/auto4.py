from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_tag_name("img")
    x_int_value = int(x_value.get_attribute("valuex"))
    answer = calc(x_int_value)
    print(answer)

    
    time.sleep(1)

    form = browser.find_element_by_id("answer")
    form.send_keys(answer)

    chkbox = browser.find_element_by_id("robotCheckbox")
    chkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    btn = browser.find_element_by_tag_name("button")
    btn.click()

    time.sleep(1)
finally:
    time.sleep(15)
    browser.quit()

