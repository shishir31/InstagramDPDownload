from bs4 import BeautifulSoup
import requests

user_name = input("Enter Instagram Username: ")
url = "https://www.instagram.com/"+user_name
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
res = requests.get(url, headers=headers)
content = res.text
bs = BeautifulSoup(content, features='html.parser')
# print(bs.prettify())
img_url = bs.find("meta",property="og:image")['content']
img_res = requests.get(img_url)
file = open(user_name+'.jpg', 'ab')
file.write(img_res.content)
file.close
print("Successful.")
# print(img_res.text)