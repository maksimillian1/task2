from django.contrib import admin
from django.urls import path
from urlapp.views import CreateShortUrl

urlpatterns = [
    path('', CreateShortUrl.as_view(), name='create_short_url'),
]
