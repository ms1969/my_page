# from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


def monday(request):
    return HttpResponse("Пойти на работу, создать ТРП")


def tuesday(request):
    return HttpResponse("Не пропустить обучение")
