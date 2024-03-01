from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.tag.models import Tag

class TagListView(ListView):
    model = Tag
    template_name = 'shop/tag/list.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_add_button'] = True # Muestra el botón de agregar
        context['add_url_variable'] = reverse_lazy('shop_tags_add') # URL de la vista de agregar
        context['shop_title'] = 'Etiquetas'
        context['title'] = 'Tag'
        return context

class TagCreateView(CreateView):
    model = Tag
    template_name = 'shop/tag/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_tags')

class TagDetailView(DetailView):
    model = Tag
    template_name = 'shop/tag/detail.html'
    context_object_name = 'tag'

class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'shop/tag/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_tags')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'shop/tag/confirm_delete.html'
    success_url = reverse_lazy('shop_tags')
