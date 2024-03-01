from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gallery

class GalleryListView(ListView):
    model = Gallery
    template_name = 'shop/gallery/list.html'
    context_object_name = 'gallery_items'

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
