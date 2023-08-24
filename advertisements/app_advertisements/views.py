from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError


def index(request):
    ads = Advertisement.objects.all()
    context = {'advertisements': ads}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')



def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            if adv.title.startswith('?'):
                raise ValidationError('Заголовок не может начинаться с вопросительного знака')
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisementForm()

    contex = {'form' : form}
    return render(request, 'advertisement-post.html', contex)