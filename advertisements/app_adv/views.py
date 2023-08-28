from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse, reverse_lazy

from .forms import AdvertisementForm
from .models import Advertisements
User=get_user_model()
def index(request):
    title=request.GET.get('query')
    if title: #не None, не пустой
        advertisements = Advertisements.objects.filter(title__icontains=title)  # результат - queryset
    else:
        advertisements=Advertisements.objects.all() #результат - queryset
    context={'advertisements': advertisements,
             'title':title
             }

    return render(request, 'app_adv/index.html', context)

def top_sellers(request):
    users=User.objects.annotate(adv_count=Count('advertisements')).order_by('-adv_count')
    context={'users':users}
    return render(request, 'app_adv/top-sellers.html', context)

@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_adv/advertisement-post.html', context)

def advertisement_detail(request, pk):
    advertisement = Advertisements.objects.get(id=pk)  # результат - queryset
    context= {'advertisement' : advertisement}
    return render(request, 'app_adv/advertisement.html', context)
