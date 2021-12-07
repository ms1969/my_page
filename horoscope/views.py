#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def zodiak_info(request, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse("Знак зодиака Лев")
    elif sign_zodiac == 'scorpio':
        return HttpResponse("Знак зодиака Скорпион")
    else:
        return HttpResponseNotFound(f"Не найден знак {sign_zodiac}")

# def leo(request):
#     return HttpResponse("Знак зодиака Лев")
#
#
# def scorpio(request):
#     return HttpResponse("Знак зодиака Скорпион")
