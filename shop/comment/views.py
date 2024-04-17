from django.views.generic import ListView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from shop.comment.models import Comment
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils.dateparse import parse_date

def comment_filtered(request):
    # Obtener datos de filtrado
    search_text = request.GET.get('text', '')
    search_user = request.GET.get('user', None)
    search_product = request.GET.get('product', None)
    search_status = request.GET.get('status', None)
    search_start_date = request.GET.get('start_date', None)
    search_end_date = request.GET.get('end_date', None)

    # Filtrar datos según los parámetros recibidos
    queryset = Comment.objects.all()
    if search_text:
        queryset = queryset.filter(text__icontains=search_text)
    if search_user:
        queryset = queryset.filter(user__id=search_user)
    if search_product:
        queryset = queryset.filter(product__id=search_product)
    if search_status is not None:
        queryset = queryset.filter(is_active=bool(int(search_status)))
    if search_start_date:
        start_date = parse_date(search_start_date)
        queryset = queryset.filter(created_at__gte=start_date)
    if search_end_date:
        end_date = parse_date(search_end_date)
        queryset = queryset.filter(created_at__lte=end_date)

    # Renderizar la tabla y devolverla como respuesta JSON
    html = render_to_string('shop/comment/table.html', {'comments': queryset}, request=request)
    return JsonResponse({'html': html})

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'shop/comment/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['show_add_button'] = True # Muestra el botón de agregar
        # context['add_url_variable'] = reverse_lazy('shop_categories_add') # URL de la vista de agregar
        context['shop_title'] = 'Comentarios'
        context['title'] = 'Comment'
        return context

class CommentDetailView(DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'shop/comment/detail.html'

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['user', 'product', 'text']
    template_name = 'shop/comment/form.html'

    def get_success_url(self):
        return reverse_lazy('comment_list')

class CommentActivateView(View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        comment.is_active = not comment.is_active  # Cambiar el estado activo/inactivo
        comment.save()

        # Aquí asumimos que quieres recargar la lista completa de comentarios
        comments = Comment.objects.all()
        html = render_to_string('shop/comment/table.html', {'comments': comments}, request=request)
        return JsonResponse({'html': html})
    