from django.contrib import admin
from django.urls import path
from urlapp.views import viewText

urlpatterns = [
    path('', viewText),
]
