from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'position', 'tittle', 'description', 'image', 'available', ('created', 'updated')]
    summernote_fields = ('description',)
    list_display = ['position', 'name', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}


# class ServiceAdmin(SummernoteModelAdmin):
#     summernote_fields = ('description', 'title',)
#
#     class Meta:
#         model = Service
#
#
# admin.site.register(Service, ServiceAdmin)
