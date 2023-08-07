from django.contrib import admin
from .models import Advertisements
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin): #админ-модель
    list_display = ['id', 'title', 'description', 'price',
                    'created_date', 'updated_date', 'auction', 'user', 'image']
    list_filter = ['auction', 'created_time']

    actions=['make_auction_false', 'make_auction_true']
    fieldsets = (
        (
            'Общее', {'fields': ('title', 'description', 'user', 'image')}
        ),
        (
            'Финансы', {'fields': ('price', 'auction'),
                        'classes': ['collapse']
                        }
        )
    )
    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Добавить возможность торга')
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisements, AdvertisementAdmin)