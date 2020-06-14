from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
path = os.path.abspath("C:/Users/User/Desktop/simple.txt")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[placeholder='Enter first name']").send_keys("Alexey")
    browser.find_element_by_css_selector("[placeholder='Enter last name']").send_keys("Erin")
    browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys("alexey@mail.ru")

    browser.find_element_by_id("file").send_keys(path)

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()