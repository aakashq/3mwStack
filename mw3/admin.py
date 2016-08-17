from django.contrib import admin
from .models import *
# Register your models here.

class SiteModelDetail(admin.ModelAdmin):
    list_display = ('name','ts','uts')
    search_fields = ('name',)

class ValueModelDetail(admin.ModelAdmin):
    list_display = ('site','a','b', 'ts', 'uts')
    search_fields = ('site','a','b',)

admin.site.register(sitemodel,SiteModelDetail)
admin.site.register(valuesmodel,ValueModelDetail)
