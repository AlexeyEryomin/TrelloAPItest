# Автоматизировннный тест на языке PYTHON для доски TRELLO с получением статус кода об успехе или провале запроса
# Тест включает в себя шаги
# Доска
# 1) Добавление доски
# 2) Получение информации о доске
# 3) Удаление доски
# Лист
# 1) Добавление доски
# 2) Получение информации о доске
# 3) Создание листа на только что созданной доске  
# 4) Получение информации о листе
# 5) Удаление созданной для теста доски чтобы не захламлять пространство в TRELLO
# Карточки
# 1) Добавление доски
# 2) Получение информации о доске
# 3) Создание листа на только что созданной доске  
# 4) Получение информации о листе 
# 5) Создание карточки на листе
# 6) Переименование карточки
# 7) Создание второго листа
# 8) Перенос карточки на второй лист
# 9) Получение информации о карточке
# 10) Добавление комментария к карточке
# 11) Удаление карточки
# 12) Удаление созданной для теста доски чтобы не захламлять пространство в TRELLO



# Переменные необходимые для использования теста для сайта TRELLO читаем внимательно заполняем и все будет работать
baseUrl = "https://www.trello.com"
# Внимание-внимание получаем токен из инструментов разработчика в браузере
myToken = "????????????????????????"
# Внимание-внимание для работы некоторых функций теста потребуется зайти на сайт ключи API для разработчиков TRELLO заходим берем ключ и второй токен именно с сайта и заполняем и все будет работать
myKey = "???????????????????????????????????????????????????????"
myToken2 = "??????????????????????????????????????????????????????????????????????"

print('Работа с досками')
print('шаг 1 Добавление доски')
import requests
import json

url = f'{baseUrl}/1/boards/'



payload = json.dumps({
  "token": f"{myToken}",
  "name": "Test",
  "defaultLists": False
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)


if response.ok:
    print ('Доска добавлена!')
else:
    print ('Не работает!')


txt = response.text
status = response.status_code

start = txt.find('"id":""') + len('"id":""')
end = txt.find(",", start)

id = txt[start:end]
id = id.replace('"', '')


print ('шаг 2 Получение информации о доске')
import requests
import json
url = f'{baseUrl}/1/boards/{id}'

payload={}

headers = {
  'Cookie': f'token={myToken2}',
  'Content-Type': 'application/json'
}

query = {
   'key': f'{myKey}',
   'token': f'{myToken2}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=query)

if response.ok:
    print ('Информация о доске получена и будет отображена в терминале!')
else:
    print ('Не работает!')

print(response.text)

print('шаг 3 Удаление доски') 

import requests
import json

url = f'{baseUrl}/1/boards/{id}'

payload = json.dumps({
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

if response.ok:
    print ('Доска успешно удалена!')
else:
    print ('Не работает!')

print('Работа с листами')
print ('шаг 1 Добавление доски')
import requests
import json

url = f'{baseUrl}/1/boards/'



payload = json.dumps({
  "token": f"{myToken}",
  "name": "Test",
  "defaultLists": False
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)


if response.ok:
    print ('Доска добавлена!')
else:
    print ('Не работает!')


txt = response.text
status = response.status_code

start = txt.find('"id":""') + len('"id":""')
end = txt.find(",", start)

id = txt[start:end]
id = id.replace('"', '')


print ('шаг 2 Получение информации о доске')
import requests
import json
url = f'{baseUrl}/1/boards/{id}'

payload={}

headers = {
  'Cookie': f'token={myToken2}',
  'Content-Type': 'application/json'
}

query = {
   'key': f'{myKey}',
   'token': f'{myToken2}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=query)

if response.ok:
    print ('Информация о доске получена и будет отображена в терминале!')
else:
    print ('Не работает!')

print(response.text)

print ('шаг 3 Создание листа на доске')
import requests
import json

url = f"{baseUrl}/1/boards/{id}/lists"

payload = json.dumps({
  "name": "Test",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data=payload)

if response.ok:
    print ('Лист успешно создан!')
else:
    print ('Не работает!')

txt2 = response.text
status2 = response.status_code

start2 = txt2.find('"id":""') + len('"id":""')
end2 = txt2.find(",", start2)

listid = txt2[start2:end2]
listid = listid.replace('"', '')

print ('шаг 4 Получение информации о листе')
import requests
import json
url = f'{baseUrl}/1/lists/{listid}'

payload={}

headers = {
  'Cookie': f'token={myToken2}',
  'Content-Type': 'application/json'
}

query = {
   'key': f'{myKey}',
   'token': f'{myToken2}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=query)

if response.ok:
    print ('Информация о листе получена и будет отображена в терминале!')
else:
    print ('Не работает!')

print(response.text)

print ('шаг 5 Удаление созданной доски чтобы не захламлять пространство в трелло')
import requests
import json

url = f'{baseUrl}/1/boards/{id}'

payload = json.dumps({
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

if response.ok:
    print ('Доска успешно удалена для того чтобы не захламлять пространство в TRELLO!')
else:
    print ('Не работает!')

print ('Работа с карточками')
print ('шаг 1 Добавление доски')
import requests
import json

url = f'{baseUrl}/1/boards/'



payload = json.dumps({
  "token": f"{myToken}",
  "name": "Test",
  "defaultLists": False
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)


if response.ok:
    print ('Доска добавлена!')
else:
    print ('Не работает!')


txt = response.text
status = response.status_code

start = txt.find('"id":""') + len('"id":""')
end = txt.find(",", start)

id = txt[start:end]
id = id.replace('"', '')


print ('шаг 2 Получение информации о доске')
import requests
import json
url = f'{baseUrl}/1/boards/{id}'

payload={}

headers = {
  'Cookie': f'token={myToken2}',
  'Content-Type': 'application/json'
}

query = {
   'key': f'{myKey}',
   'token': f'{myToken2}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=query)

if response.ok:
    print ('Информация о доске получена и будет отображена в терминале!')
else:
    print ('Не работает!')

print(response.text)

print ('шаг 3 Создание листа на доске')
import requests
import json

url = f"{baseUrl}/1/boards/{id}/lists"

payload = json.dumps({
  "name": "Test",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data=payload)

if response.ok:
    print ('Лист успешно создан!')
else:
    print ('Не работает!')

txt2 = response.text
status2 = response.status_code

start2 = txt2.find('"id":""') + len('"id":""')
end2 = txt2.find(",", start2)

listid = txt2[start2:end2]
listid = listid.replace('"', '')

print ('шаг 4 Получение информации о листе')
import requests
import json
url = f'{baseUrl}/1/lists/{listid}'

payload={}

headers = {
  'Cookie': f'token={myToken2}',
  'Content-Type': 'application/json'
}

query = {
   'key': f'{myKey}',
   'token': f'{myToken2}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=query)

if response.ok:
    print ('Информация о листе получена и будет отображена в терминале!')
else:
    print ('Не работает!')

print(response.text)

print ('шаг 5 Создание карточки на только что созданном листе')
import requests
import json

url = f"{baseUrl}/1/lists/{listid}/cards"

payload = json.dumps({
  "name": "Test",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.ok:
    print ('Карточка на новом листе успешно создана!')
else:
    print ('Не работает!')

txt3 = response.text
status3 = response.status_code

start3 = txt3.find('"id":""') + len('"id":""')
end3 = txt3.find('","', start3)

cardid = txt3[start3:end3]
cardid = cardid.replace('"', '')
cardid = cardid[47:]

print(response.text)
print(cardid)
print ('шаг 6 Переименование созданной карточки')
import requests
import json

url = f"{baseUrl}/1/cards/{cardid}"

payload = json.dumps({
  "name": "Rename Test",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

if response.ok:
    print ('Карточка успешно переименована!')
else:
    print ('Не работает!')

print ('шаг 7 Создание второго листа')

import requests
import json

url = f"{baseUrl}/1/boards/{id}/lists"

payload = json.dumps({
  "name": "Test2",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data=payload)

if response.ok:
    print ('Лист 2 успешно создан!')
else:
    print ('Не работает!')

txt4 = response.text
status4 = response.status_code

start4 = txt4.find('"id":""') + len('"id":""')
end4 = txt4.find(",", start4)

listid2 = txt4[start4:end4]
listid2 = listid2.replace('"', '')

print ('шаг 8 Перенос карточки на второй лист')
import requests
import json

url = f"{baseUrl}/1/cards/{cardid}"

payload = json.dumps({
  "idList": f"{listid2}",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

if response.ok:
    print ('Карточка успешно перенесена!')
else:
    print ('Не работает!')


print('шаг 9 получение информации о карточке')
import requests

url = f"{baseUrl}/1/cards/{cardid}"

payload={}

headers = {
  'Cookie': f'token={myToken2}',
  'Content-Type': 'application/json'
}

query = {
   'key': f'{myKey}',
   'token': f'{myToken2}'
}

response = requests.request("GET", url, headers=headers, data=payload, params=query)

if response.ok:
    print ('Информация о карточке получена и будет отображена в терминале!')
else:
    print ('Не работает!')

print(response.text)


print ('шаг 10 Добавление комментария к карточке')
import requests
import json

url = f"{baseUrl}/1/cards/{cardid}/actions/comments"

payload = json.dumps({
  "text": "Comment Test",
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.ok:
    print ('Комментарий успешно добавлен!')
else:
    print ('Не работает!')

print ('шаг 11 Удаление карточки')
import requests
import json

url = f"{baseUrl}/1/cards/{cardid}"

payload = json.dumps({
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

if response.ok:
    print ('Карточка успешно удалена!')
else:
    print ('Не работает!')

print ('шаг 12 Удаление созданной для теста доски чтобы не захламлять пространство в TRELLO')
import requests
import json

url = f'{baseUrl}/1/boards/{id}'

payload = json.dumps({
  "token": f"{myToken}"
})
headers = {
  'Cookie': f'token={myToken}',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

if response.ok:
    print ('Доска успешно удалена и не оставит следов в пространстве TRELLO!')
else:
    print ('Не работает!')

print("Test Trello API завершен")    
