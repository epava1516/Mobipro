from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView
from django.urls import reverse_lazy, reverse
from shop.product.models import Product
from django.shortcuts import get_object_or_404

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_add_button'] = True # Muestra el botón de agregar
        context['add_url_variable'] = reverse_lazy('shop_products_add') # URL de la vista de agregar
        context['shop_title'] = 'Productos'
        context['title'] = 'Product'
        return context

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/product/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_products')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'shop/product/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_products')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product/confirm_delete.html'
    success_url = reverse_lazy('shop_products')

class ProductActivateView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.is_active = False
        product.save()
        return reverse('shop_products')