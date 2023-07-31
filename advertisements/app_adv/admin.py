from django.contrib import admin
from .models import Advertisements
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advertisements, AdvertisementAdmin)