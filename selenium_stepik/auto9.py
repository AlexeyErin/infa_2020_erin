from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # button = WebDriverWait(browser, 1).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(browser.find_element_by_id("input_value").text))

    browser.find_element_by_id("solve").click()


finally:
    time.sleep(5)
    browser.quit()