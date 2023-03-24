from django.contrib import admin
from .models import Menu, MenuItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)

class MenuAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'description')
    search_fields = ['name', 'description']
    list_filter = ('name', 'description')
    summernote_fields = ('content',)


@admin.register(MenuItem)

class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'created_on')
    list_filter = ('description', 'name')
    search_fields = ('name', 'allegen', 'description')


