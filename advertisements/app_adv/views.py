from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import AdvertisementForm
from .models import Advertisements

def index(request):
    advertisements=Advertisements.objects.all() #результат - queryset
    context={'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    form=AdvertisementForm()
    context={'form':form}
    return render(request, 'advertisement-post.html', context)

