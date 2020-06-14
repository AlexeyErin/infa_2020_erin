from selenium import webdriver
import time

link =  "http://suninjuly.github.io/registration1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
    input2.send_keys("Koshkin")
    input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
    input3.send_keys("KoshkinIv@mail.ru")
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    time.sleep(1)

    result = browser.find_element_by_tag_name("h1")
    text_of_result = result.text
    assert "Congratulations! You have successfully registered!" == text_of_result

finally:
    time.sleep(5)
    browser.quit()



