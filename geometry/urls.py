from django.urls import path, converters
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:figure>', views.figure, name='geometry-name'),
]
