# beauty_shop/apps/blog/views.py
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


# ========================
# 📄 Vista de lista de publicaciones
# ========================
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']


# ========================
# 📝 Vista de detalle de publicación + comentarios
# ========================
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        """
        Añade comentarios aprobados y formulario vacío al contexto.
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(approved=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Procesa el envío de comentarios desde el mismo detalle del post.
        """
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            messages.success(request, "Tu comentario ha sido enviado para revisión.")
            return redirect('blog:post_detail', slug=self.object.slug)
        else:
            context = self.get_context_data()
            context['comment_form'] = form
            return self.render_to_response(context)
