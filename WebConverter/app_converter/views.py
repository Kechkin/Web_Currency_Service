from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

DB = {
    "Рубль": {
        "00:00": {
            "course": "1"
        },
    },
}


def index(request):
    context2 = {
        "DB": DB.keys()
    }
    return render(request, 'app_converter/index.html', context2)


# поиск по БД
def search_data(request):
    context, start_time_current, course = {}, '', ''
    if request.method == "POST":
        currency = request.POST['currency']
        time_data = request.POST['time']
        # проверка на наличие ключа
        if currency in DB:
            if time_data:
                for i in DB[currency].keys():
                    if time_data >= i:
                        course = DB[currency][i]["course"]
                        start_time_current = i
            else:
                # поиск по последнему добавленному по дате
                time_data = max(DB[currency].keys())
                course = DB[currency][time_data]["course"]
        else:
            return HttpResponse("Такой валюты нет или ввели ошибочно")
        context = {
            "currency": currency,
            "course": course,
            "time": start_time_current or time_data
        }
        return render(request, 'app_converter/search_data.html', context)


# добавить курс в БД

def add_data(request):
    if request.method == "POST":
        time_data = datetime.now().strftime("%H:%M")  # ("%H:%M %d-%m-%y) - добавить с датой
        currency = request.POST['currency']
        course = request.POST['course']
        # добавляем в БД пришедшие данные
        if currency and course:
            if currency in DB:
                DB[currency][time_data] = {"course": course}
            else:
                DB[currency] = {time_data: {"course": course}}
        else:
            return HttpResponse("Вы не ввели данные")
    return render(request, 'app_converter/add_data.html')


def converterTo(request):
    context = {}
    if request.method == "POST":
        currency = request.POST['currency']
        currency2 = request.POST['currency2']
        money = request.POST['money']
        if currency in DB and currency2 in DB and money:
            # поиск по послед. добавленному курсу
            time_data = max(DB[currency].keys())
            time_data2 = max(DB[currency2].keys())
            course = DB[currency][time_data]["course"]
            course2 = DB[currency2][time_data2]["course"]
            result = "%.2f" % ((float(money) * float(course)) / float(course2))
            context = {
                "money": money,
                "currency": currency,
                "currency2": currency2,
                "course": course,
                "result": result,
                "DB": DB.keys()
            }
        return render(request, 'app_converter/converterTo.html', context)
    elif request.method == "GET":
        context2 = {
            "DB": DB.keys()
        }
        return render(request, 'app_converter/converterTo.html', context2)
