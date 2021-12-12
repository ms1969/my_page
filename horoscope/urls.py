from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>', views.zodiak_info_num),
    path('<str:sign_zodiac>', views.zodiak_info, name='horoscope-name')
]
