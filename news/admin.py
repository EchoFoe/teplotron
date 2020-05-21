from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'tittle', 'description', 'image', 'available', ('created', 'updated')]
    list_display = ['name', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
