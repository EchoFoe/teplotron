from django.contrib import admin
from .models import AboutUs, AboutUsDetails, Partners, Customer


class AboutUsDetailsInline(admin.TabularInline):
    model = AboutUsDetails
    extra = 0


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['name', 'tittle', 'description', 'image', 'available', 'address', ('email', 'phone'), ('schedule_start', 'schedule_end'), ('created', 'updated')]
    list_display = ['name', 'available']
    list_editable = ['available']
    # inlines = [AboutUsDetailsInline]
    list_filter = ['available', 'created', 'updated']


# @admin.register(Partners)
# class PartnersAdmin(admin.ModelAdmin):
#     save_as = True
#     fields = ['name', 'image', 'available', ('created', 'updated')]
#     list_display = ['name', 'available']
#     list_editable = ['available']
#     list_filter = ['available', 'created', 'updated']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'status', ('created', 'updated')]
    list_display = ['first_name', 'last_name', 'email', 'phone', 'status']
    list_filter = ['status', 'created', 'updated']


# @admin.register(AboutUsDetails)
# class AboutUsDetailsAdmin(admin.ModelAdmin):
#     save_as = True
#     fields = ['name', ('is_main', 'is_not_main', 'available'), 'email', 'phone', 'address', ('schedule_start', 'schedule_end'), ('created', 'updated')]
#     list_display = ['name', 'is_main', 'is_not_main', 'available']
#     list_filter = ['name', 'is_main', 'is_not_main', 'available']
#     list_editable = ['is_main', 'is_not_main', 'available']
