import requests

url = 'https://dev.airhubstore.com/'
page = requests.get(url, auth=('feshchenko.vitalii@gmail.com', '1522'))
print(page.status_code)
print(page.content)
print(page.text)

