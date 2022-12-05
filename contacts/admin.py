from django.contrib import admin

from .models import Contact, Form

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','car_title','create_date')
    list_display_links = ('id','first_name','car_title',)
    search_fields = ('id','first_name','last_name','car_title','email')
    list_per_page = 25
admin.site.register(Contact, ContactAdmin)

class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    list_display_links = ('first_name',)
    search_fields = ('first_name','last_name','email')

admin.site.register(Form, FormAdmin)
