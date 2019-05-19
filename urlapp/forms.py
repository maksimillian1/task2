from django import forms
from .models import ShorterUrl

class UrlForm(forms.Form):
    base_url = forms.URLField(max_length=100)

    def save(self, short):
        return  ShorterUrl.objects.create(
            base_url=self.cleaned_data['base_url'],
            short_url=short
        )
