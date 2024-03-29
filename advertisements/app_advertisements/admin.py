from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'description', 'price', 
                    'created_date', 'updated_date', 'auction', 'image_tag']
    list_filter = ['auction', 'created_at']
    actions = ['change_auction_as_false', 'change_auction_as_True']
    fieldsets = (
        (
            'Общее', {
                'fields' : ('title', 'description', 'image')
                }
        ),

        (
            'Финансы', {
                'fields' : ('price', 'auction'),
                'classes' : ['collapse']
                }
        ),

    )
    
    # У выделенных объектов заменяет значение поля "торг" на "нет"
    @admin.action(description="Убрать возможность торга")
    def change_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def change_auction_as_True(self, request, queryset):
        queryset.update(auction=True)



admin.site.register(Advertisement, AdvertisementAdmin)