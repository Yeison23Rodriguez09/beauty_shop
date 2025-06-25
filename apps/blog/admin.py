# beauty_shop/apps/blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment

# ========================
# 📂 Categorías
# ========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)


# ========================
# 📝 Publicaciones
# ========================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created_at')
    list_filter = ('published', 'created_at', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


# ========================
# 💬 Comentarios
# ========================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'name', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'content', 'author__username')
    actions = ['approve_comments']
    readonly_fields = ('created_at',)

    @admin.action(description="Aprobar comentarios seleccionados")
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
