# beauty_shop/apps/blog/models.py
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


# ========================
# 📂 Categoría
# ========================
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

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})


# ========================
# 📝 Publicación
# ========================
class Post(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", max_length=220, unique=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Autor"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name="Categoría"
    )
    content = models.TextField("Contenido")
    image = models.ImageField(
        "Imagen de Portada",
        upload_to='blog/images/',
        null=True,
        blank=True
    )
    published = models.BooleanField("Publicado", default=True)

    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


# ========================
# 💬 Comentario
# ========================
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Publicación"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Autor (registrado)"
    )
    name = models.CharField("Nombre (invitado)", max_length=100, blank=True)
    content = models.TextField("Comentario")
    approved = models.BooleanField("Aprobado", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['created_at']

    def __str__(self):
        author_name = self.author.get_username() if self.author else (self.name or "Anónimo")
        return f"Comentario de {author_name} en '{self.post.title}'"
