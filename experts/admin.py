from django.contrib import admin
from .models import Expert


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('first_name', 'last_name'), ('position', 'office'), ('country', 'town'), ('phone', 'email'), 'image', 'dob', 'description', ('vk', 'instagram'), ('twitter', 'facebook'), 'available', ('created', 'updated')]
    list_display = ['first_name', 'last_name', 'phone', 'email', 'available', 'office']
    list_editable = ['phone', 'email', 'available']
    list_filter = ['available']
    search_fields = ['first_name', 'last_name']

