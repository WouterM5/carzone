from django.contrib import admin
from django.utils.html import format_html
from .models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="60" style="border-radius:50%;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('id','thumbnail','car_title','transmission','created_date','is_featured',)
    list_display_links = ('id','thumbnail','car_title',)
    search_fields = ('car_title','is_featured' )
    list_editable = ('is_featured',)
    list_filter = ('is_featured',)
    ordering = ('id',)
    

admin.site.register(Car, CarAdmin)