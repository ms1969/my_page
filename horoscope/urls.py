from django.urls import path, converters
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:sign_zodiac>', views.zodiak_info_num),
    path('<str:sign_zodiac>', views.zodiak_info, name='horoscope-name'),
#    path('<type_zodiac>', views.type_zodiac_info, name='type-name'),
]
