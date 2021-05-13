from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Reddit:

    def __init__(self):
        self.driver = webdriver.Chrome()


    def open_all_tabs(self):
        with open('./keys', 'r') as file:
            content = file.readlines()
            self.keys = [i.split('\n')[0] for i in content]
            file.close()
        for key in self.keys:
            next_tab = input()
            if next_tab:
                URL = f"https://www.reddit.com/search/?q={key}&sort=new"
                self.driver.get(URL)
                # open tab
                # self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
                # self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
                # time.sleep(10)

    def new_tab(self):
        URL = f"https://www.reddit.com/search/?q=1&sort=new"
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        self.driver.get(URL)

