from django.contrib import admin
from django.urls import path
from urlapp.views import CreateShortUrl, list_urls

urlpatterns = [
    path('', CreateShortUrl.as_view(), name='create_short_url'),
    path('/urls', list_urls, name='urls_url')
]
