from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'position', 'mention', 'file', 'available', ('created', 'updated')]
    list_display = ['position', 'name', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
