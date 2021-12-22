from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_type),
    path('<type_zodiac>', views.type_zodiac_info, name='type-name'),
]
