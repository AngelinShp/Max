from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse

from .forms import AdvertisementForm
from .models import Advertisements

def index(request):
    advertisements=Advertisements.objects.all() #результат - queryset
    context={'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)

