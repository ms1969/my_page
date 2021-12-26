from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


def monday(request):
    return render(request, "week_days/greeting.html")


def tuesday(request):
    return HttpResponse("Не пропустить обучение")
