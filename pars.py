from email import header
from nturl2path import url2pathname
from re import L
import requests
from bs4  import BeautifulSoup


url= "https://int.soccerway.com/matches/2022/07/30/russia/premier-league/fk-zenit-sankt-petersburg/fk-lokomotiv-moscow/3806710/"

#заполняем заголовки что бы не словить ошибку 403
headers={
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.148 YaBrowser/22.7.2.902 Yowser/2.5 Safari/537.36",
}

req= requests.get(url,headers=headers)
src= req.text

# Сохраняем html файл на случай ,если не будет доступа
with open("index.html","w",encoding="utf-8") as file:
    src = file.write(src)

with open('index.html') as file:
    src= file.read()

soup= BeautifulSoup(src, "lxml")
#Фильтруем поиск
lineups= soup.find_all(class_='playerstats lineups table')
for item in lineups:
    item_text= item.text
    print (f"{item_text}")

#Выводим результат
file = open('res.txt', 'w', encoding='utf-8')
file.write(item_text)

