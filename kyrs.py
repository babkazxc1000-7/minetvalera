import requests#импорт библиотеки
import json
username=input("Введите никнейм:")
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
data = response.json()
if response.status_code == 200:#если код 200(всё успешно)
    print("Сервер ответил успешно")
    with open("kurs.json" , "w", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False, indent=4)
    print("Файл создан")
    with open("kurs.txt" , "w", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False, indent=4)
    print("Файл создан")
else:
    print("Юзер не найден, ошибкО!!!",response.status_code)
        
