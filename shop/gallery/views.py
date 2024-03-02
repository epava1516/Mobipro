from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gallery

class GalleryListView(ListView):
    model = Gallery
    template_name = 'shop/gallery/list.html'
    context_object_name = 'gallery_items'
    paginate_by = 10  # Opcional: para paginar los resultados

    def get_queryset(self):
        queryset = super().get_queryset()
        # Aplicar filtros según los parámetros recibidos en la solicitud GET
        user = self.request.GET.get('user')
        status = self.request.GET.get('status')
        if user:
            queryset = queryset.filter(user__icontains=user)
        if status == 'active':
            queryset = queryset.filter(is_active=True)
        elif status == 'inactive':
            queryset = queryset.filter(is_active=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_title'] = 'Galerias'
        context['title'] = 'Gallery'
        return context


class GalleryCreateView(CreateView):
    model = Gallery
    template_name = 'shop/gallery/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_gallery')

class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'shop/gallery/detail.html'
    context_object_name = 'gallery_item'

class GalleryUpdateView(UpdateView):
    model = Gallery
    template_name = 'shop/gallery/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_gallery')

class GalleryDeleteView(DeleteView):
    model = Gallery
    template_name = 'shop/gallery/confirm_delete.html'
    success_url = reverse_lazy('shop_gallery')
