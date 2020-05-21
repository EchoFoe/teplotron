from django.contrib import admin
from .models import Portfolio, PortfolioDetails


class PortfolioDetailsInline(admin.TabularInline):
    model = PortfolioDetails
    extra = 0


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('name', 'slug'), 'image', 'description', 'available', ('created', 'updated')]
    list_display = ['name', 'available']
    inlines = [PortfolioDetailsInline]
    list_filter = ['name', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PortfolioDetails)
class PortfolioDetailsAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['portfolio', 'available', 'image', ('created', 'updated')]
    list_display = ['portfolio', 'available']
    list_filter = ['portfolio', 'available']
    list_editable = ['available']
