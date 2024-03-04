from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.category.models import Category
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse

def category_filtered(request):
    # Obtener datos de filtrado
    search_input = request.GET.get('q', None)
    search_state = request.GET.get('state', None)

    # Filtrar datos según los parámetros recibidos
    queryset = Category.objects.all()
    if search_input:
        queryset = queryset.filter(name__icontains=search_input) | queryset.filter(description__icontains=search_input)
    if search_state:
        queryset = queryset.filter(is_active=bool(int(search_state)))

    # Renderizar la tabla y devolverla como respuesta JSON
    html = render_to_string('shop/category/table.html', {'categories': queryset})
    return JsonResponse({'html': html})

class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category/list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        state = self.request.GET.get('state')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if state:
            queryset = queryset.filter(is_active=bool(int(state)))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_add_button'] = True  # Muestra el botón de agregar
        context['add_url_variable'] = reverse_lazy('shop_categories_add')  # URL de la vista de agregar
        context['shop_title'] = 'Categorías'
        context['title'] = 'Category'
        return context

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'shop/category/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url_variable'] = reverse_lazy('shop_categories')  # URL de la vista de agregar
        context['shop_title'] = 'Añadir Categoría'
        context['title'] = 'Category'
        context['action'] = 'Añadir'
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category/detail.html'
    context_object_name = 'category'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'shop/category/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_categories')

    def get_success_url(self):
        # print(self.object.pk)
        return reverse_lazy('shop_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = context.get('object')
        print(dir(self))
        print(self.get_success_url())
        context['list_url_variable'] = reverse_lazy('shop_categories')  # URL de la vista de agregar
        context['shop_title'] = 'Editar Categoría'
        context['title'] = 'Category'
        context['action'] = 'Editar'
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/category/confirm_delete.html'
    success_url = reverse_lazy('shop_categories')
