# beauty_shop/apps/catalog/models.py
from django.db import models
from django.utils.text import slugify
import os


# 🖼️ Ruta dinámica: inventario/img/categoria/producto/imagen.jpg
def product_image_upload_path(instance, filename):
    categoria = slugify(instance.category.name)
    producto = slugify(instance.name)
    return f'inventario/img/{categoria}/{producto}/{filename}'


# 📂 Categoría de producto
class Category(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)
    slug = models.SlugField("Slug", max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# 🏷️ Marca
class Brand(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['name']

    def __str__(self):
        return self.name


# 🛍️ Producto
class Product(models.Model):
    name = models.CharField("Nombre", max_length=200)
    slug = models.SlugField("Slug", max_length=220, unique=True, blank=True)
    description = models.TextField("Descripción", blank=True)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Stock", default=0)
    image = models.ImageField("Imagen principal", upload_to=product_image_upload_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoría")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="Marca")
    is_active = models.BooleanField("Activo", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
