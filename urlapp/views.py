from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from pyshorteners import Shortener
from .models import ShorterUrl

from .models import ShorterUrl
from .forms import UrlForm


def list_urls(request):
    urls = ShorterUrl.objects.all()
    return render(request, 'urlapp/url-stats.html', context={'urls': urls})
    

class CreateShortUrl(View):

    def get(self, request):
        form = UrlForm()
        return render(request, 'urlapp/index.html', context={'form': form})

    def post(self, request):
        url = UrlForm(request.POST)

        if url.is_valid():
            shortener = Shortener('Isgd')
            new_url = url.save(shortener.short(url.cleaned_data['base_url']))
            messages.info(request, new_url.short_url)
            return render(request, 'urlapp/index.html')
