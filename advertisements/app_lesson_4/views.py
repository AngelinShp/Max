from django.http import HttpResponse


# Create your views here.
def homework(request):
    return HttpResponse('Домашка по 4 занятию')


