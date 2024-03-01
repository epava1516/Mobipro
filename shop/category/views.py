from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.category.models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category/list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_add_button'] = True # Muestra el botón de agregar
        context['add_url_variable'] = reverse_lazy('shop_categories_add') # URL de la vista de agregar
        context['shop_title'] = 'Categorías'
        context['title'] = 'Category'
        return context

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'shop/category/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_categories')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category/detail.html'
    context_object_name = 'category'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'shop/category/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_categories')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/category/confirm_delete.html'
    success_url = reverse_lazy('shop_categories')
