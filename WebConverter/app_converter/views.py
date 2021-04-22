from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.template import loader

DB = {
    "Евро": {
        "12:40": {
            "course": "40"
        },
        "12:50": {
            "course": "50"
        },
        "13:00": {
            "course": "60"
        }
    },
    "Доллар": {
        "12:41": {
            "course": "84.2"
        },
        "12:45": {
            "course": "84.5"
        }
    }
}


def index(request):
    return render(request, 'app_converter/index.html')


# поиск по БД
def search_data(request):
    context = ''
    res = {}
    if request.method == "POST":
        currency = request.POST['currency']
        time_data = request.POST['time']
        # проверка на наличие ключа
        if currency in DB:
            if time_data:
                for i in DB[currency].keys():
                    if time_data >= i:
                        context = DB[currency][i]["course"]
            else:
                # поиск по последнему добавленному по дате
                time_data = max(DB[currency].keys())
                context = DB[currency][time_data]["course"]
        else:
            return HttpResponse("Такой валюты нет или ввели ошибочно")
        res = {
            "currency": currency,
            "course": context,
            "time": time_data
        }
    return render(request, 'app_converter/search_data.html', res)


# добавить курс в БД

def add_data(request):
    if request.method == "POST":
        time_data = datetime.now().strftime("%H:%M:%S")
        currency = request.POST['currency']
        course = request.POST['course']
        # добавляем в БД пришедшие данные
        if currency in DB:
            DB[currency][time_data] = {"course": course}
        else:
            DB[currency] = {time_data: {"course": course}}
    return HttpResponse("данные отправлены")
