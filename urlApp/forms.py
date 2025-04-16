from django import forms 
from .models import ShortURL


class CreateShortUrl(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url']

        widgets = {
            'original_url': forms.TextInput(attrs={'class':'form-control'}),
        }