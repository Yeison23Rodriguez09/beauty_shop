# beauty_shop/apps/blog/forms.py
from django import forms
from .models import Post, Comment

# ========================
# 📝 Formulario de Publicación
# ========================
class PostForm(forms.ModelForm):
    """
    Formulario para crear o editar entradas del blog por parte de un autor.
    """
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'image', 'published')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Escribe el contenido aquí...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


# ========================
# 💬 Formulario de Comentario
# ========================
class CommentForm(forms.ModelForm):
    """
    Formulario para que visitantes registrados o anónimos agreguen comentarios.
    """
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre (opcional si has iniciado sesión)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu comentario...'
            }),
        }
