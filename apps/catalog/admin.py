# beauty_shop/apps/catalog/admin.py
from django.contrib import admin
from .models import Category, Brand, Product


# ========================
# 📂 Admin de Categorías
# ========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)


# ========================
# 🏷️ Admin de Marcas
# ========================
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# ========================
# 🛍️ Admin de Productos
# ========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'category', 'brand',
        'is_active', 'created_at'
    )
    list_filter = (
        'is_active', 'category', 'brand', 'created_at'
    )
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    autocomplete_fields = ('category', 'brand')
