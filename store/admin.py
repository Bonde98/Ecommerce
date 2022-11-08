from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price',
                    'in_stock','created','update']
    list_editable = ['price','in_stock']
    list_filter = ['is_active','in_stock']
    prepopulated_fields = {'slug':('title',)}