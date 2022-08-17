from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_filter, name='select_filter')
]