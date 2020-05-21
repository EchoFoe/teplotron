from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'position', 'tittle', 'description', 'image', 'available', ('created', 'updated')]
    list_display = ['position', 'name', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
