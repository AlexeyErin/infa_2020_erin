from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    numbers = str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text))

    browser.find_element_by_tag_name("select").click()
    target = browser.find_element_by_css_selector('[value=' + '"' + numbers + '"' + ']').click()

    btn = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(8)
    browser.quit()

