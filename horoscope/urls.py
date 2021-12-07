from django.urls import path
from . import views

urlpatterns = [
    path('<sign_zodiac>/', views.zodiak_info),
]