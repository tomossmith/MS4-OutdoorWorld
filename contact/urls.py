""" Contact App - urls.py """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact, name="contact"),
]
