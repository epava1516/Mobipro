from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.comment.models import Comment

class CommentListView(ListView):
    model = Comment
    template_name = 'shop/comment/list.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['show_add_button'] = True # Muestra el botón de agregar
        # context['add_url_variable'] = reverse_lazy('shop_categories_add') # URL de la vista de agregar
        context['shop_title'] = 'Comentarios'
        context['title'] = 'Comment'
        return context

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'shop/comment/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_comments')

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'shop/comment/detail.html'
    context_object_name = 'comment'

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'shop/comment/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_comments')

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'shop/comment/confirm_delete.html'
    success_url = reverse_lazy('shop_comments')
