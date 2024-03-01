from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.product.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'

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
