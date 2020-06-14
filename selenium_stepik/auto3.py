from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

brows = webdriver.Chrome()
brows.get(link)

texts = brows.find_elements_by_css_selector("[type='text']")
for text in texts:
    text.send_keys("Something")
button = brows.find_element_by_css_selector("[type='submit']")
button.click()