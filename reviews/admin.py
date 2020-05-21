from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('first_name', 'last_name'), 'message', 'image', 'available', ('created', 'updated')]
    list_display = ['last_name', 'first_name', 'Отзыв', 'available', 'created', 'id']
    list_filter = ['available', 'last_name', 'created', 'updated']
    list_editable = ['available']
    search_fields = ['last_name']
