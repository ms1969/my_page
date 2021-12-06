from . import views
from django.urls import path

urlpatterns = [
    path('monday/', views.monday),
    path('tuesday/', views.tuesday),
]
