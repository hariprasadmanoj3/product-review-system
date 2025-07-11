from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_by', 'average_rating', 'review_count', 'created_at')
    list_filter = ('created_at', 'is_active')
    search_fields = ('name', 'description')
    readonly_fields = ('average_rating', 'review_count')