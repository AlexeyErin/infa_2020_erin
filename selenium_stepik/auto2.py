from selenium import webdriver
import time

link = "https://www.ozon.ru/category/yuvelirnye-ukrasheniya-50001/?text=mac&from_global=true"

browser = webdriver.Chrome()
browser.get(link)

goods = browser.find_elements_by_css_selector("[class='a3q6 a3q7'] .ui-a9")
for good in goods:
    good.click()

print(len(goods))
