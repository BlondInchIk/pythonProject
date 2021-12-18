import requests
import json
from datetime import datetime
from  main import FIO

#Возвращает рассписание в виде json
def rasp():
    ID = "https://ruz.hse.ru/api/search?term=" + FIO
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50"}

    full_page = requests.post(ID, headers=headers)
    full_page_str = str(full_page.content, 'utf8')

    string = json.loads(full_page_str)
    if string == []:
        return "Пользователь не найден!"

    cur_id = ""
    for i in string:
        string2 = dict(i)
        if string2.get("id") != "":
            cur_id = string2.get("id")
        break

    raspisanie = "https://ruz.hse.ru/api/schedule/student/" + str(cur_id) + "?start=" + str(year) + "." + str(month) + "." + str(day) + "&finish=" + str(year) + "." + str(month) + "." + str(day+7)

    full_page = requests.post(raspisanie, headers=headers)
    full_page_str = str(full_page.content, 'utf8')
    string = json.loads(full_page_str)

    if string == []:
        return "Пользователь не найден!"
    return string