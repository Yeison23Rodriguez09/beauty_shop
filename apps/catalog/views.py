# beauty_shop/apps/catalog/views.py
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Product, Category


# ========================
# 🛍️ Vista de listado de productos
# ========================
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        """
        Devuelve productos activos, filtrados por categoría si se especifica.
        """
        queryset = Product.objects.filter(is_active=True).select_related('category', 'brand')
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Añade las categorías disponibles al contexto para el filtro lateral/menu.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.kwargs.get('category_slug')
        return context


# ========================
# 🔍 Vista de detalle de producto
# ========================
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        """
        Filtra solo productos activos (evita mostrar eliminados o desactivados).
        """
        return Product.objects.filter(is_active=True).select_related('category', 'brand')
