import requests
from bs4 import BeautifulSoup as BS
import datetime
from selenium import webdriver


driver = webdriver.Chrome()
today = datetime.datetime.now()
date = today.strftime('%d-%m-%y')
url = 'https://iev.aero/ru/departures?date=' + date
driver.get(url)
class_1 = driver.find_element_by_class_name('tabs-container')
class_2 = driver.find_element_by_class_name('time-field')
selectors = driver.find_elements_by_css_selector('td')

sort_in_list = [element.text for element in selectors]
#print(sort_in_list)
print(sort_in_list[0])
driver.close()






