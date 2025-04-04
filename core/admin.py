from django.contrib import admin
from .models import Customer, Product, Order, Category

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company')
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer__name', 'product__name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']