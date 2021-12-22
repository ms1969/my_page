# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

dict_zodiac = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
               "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
               "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
               "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
               "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
               "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
               "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
               "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
               "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
               "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
               "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
               "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)",
               }

dict_type = {"fire": ["aries", "leo", "sagittarius"],
             "earth": ["taurus", "virgo", "capricorn"],
             "air": ["gemini", "libra", "aquarius"],
             "water": ["cancer", "scorpio", "pisces"]
             }


def index(request):
    zodiacs = list(dict_zodiac)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    responce = f"""
    <ul>
        {li_elements}
    <ul/>
    """
    return HttpResponse(responce)


def zodiak_info(request, sign_zodiac: str):
    description = dict_zodiac.get(sign_zodiac)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f"Не найден знак {sign_zodiac}")


def zodiak_info_num(request, sign_zodiac: int):
    zodiacs = list(dict_zodiac)
    if sign_zodiac > len(zodiacs) or sign_zodiac == 0:
        return HttpResponseNotFound(f"Не найден знак c номером {sign_zodiac}")
    else:
        name_zodiac = zodiacs[sign_zodiac - 1]
        redirect_url = reverse('horoscope-name', args=[name_zodiac])
        return HttpResponseRedirect(redirect_url)


def type_zodiac_info(request, type_zodiac):
    description = dict_type.get(type_zodiac)
    li_elements = ''
    for sign in description:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    responce = f"""
    <ul>
        {li_elements}
    <ul/>
    """
    return HttpResponse(responce)

def index_type(request):
        type_zodiacs = list(dict_type)
        li_elements = ''
        for sign_type in type_zodiacs:
            redirect_path = reverse('type-name', args=[sign_type])
            li_elements += f"<li> <a href='{redirect_path}'>{sign_type.title()} </a> </li>"
        responce = f"""
        <ul>
            {li_elements}
        <ul/>
        """
        return HttpResponse(responce)
