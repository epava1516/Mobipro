from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.comment.models import Comment

class CommentListView(ListView):
    model = Comment
    template_name = 'shop/comment/list.html'
    context_object_name = 'comments'

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
