from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = 'Fox Automation administration'
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration'

@admin.register(Categories)
class CataAdmin(admin.ModelAdmin):
    list_display= ['catagory_name']
    list_filter = ['catagory_name']

@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'person_whatsapp_no', 'catagory']
    list_filter = ['person_name', 'catagory']


