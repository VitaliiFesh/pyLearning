from selenium import webdriver

class Reddit:

    def __init__(self):
        self.driver = webdriver.Chrome()
        with open('./keys', 'r') as file:
            content = file.readlines()
            self.keys = [i.split('\n')[0] for i in content]
            file.close()
        self.key_in_list = iter(self.keys)

    def next_tab(self):

        next_key = next(self.key_in_list)
        URL = f"https://www.reddit.com/search/?q={next_key}&sort=new"
        self.driver.get(URL)

