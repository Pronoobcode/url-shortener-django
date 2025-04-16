from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
import random, string
from .models import ShortURL
from .forms import CreateShortUrl
# Create your views here.


def home_view(request):
    return render(request, 'urlApp/home.html')


def create_url_view(request):
    form = CreateShortUrl()
    if request.method == 'POST':
        form = CreateShortUrl(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            random_chars_lst = list(string.ascii_letters)
            random_chars = ''.join(random.choices(random_chars_lst, k=6))

            while ShortURL.objects.filter(short_url=random_chars).exists():
                random_chars = ''.join(random.choices(random_chars_lst, k=6))

            short_url = ShortURL(original_url=original_url, short_url=random_chars)
            short_url.save()
            return render(request, 'urlApp/urlcreated.html', {'chars': random_chars})

    return render(request, 'urlApp/create.html', {'form': form})


def redirect_view(request, url):
    current_obj = get_object_or_404(ShortURL, short_url=url)
    return redirect(current_obj.original_url)
