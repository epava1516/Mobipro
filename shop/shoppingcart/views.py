from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.shoppingcart.models import ShoppingCart

class ShoppingCartListView(ListView):
    model = ShoppingCart
    template_name = 'shop/shoppingcart/list.html'
    context_object_name = 'shopping_carts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['show_add_button'] = True # Muestra el botón de agregar
        # context['add_url_variable'] = reverse_lazy('shop_coupons_add') # URL de la vista de agregar
        context['shop_title'] = 'Carritos de compra'
        context['title'] = 'Shopping Cart'
        return context

class ShoppingCartCreateView(CreateView):
    model = ShoppingCart
    template_name = 'shop/shoppingcart/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_shopping_cart')

class ShoppingCartDetailView(DetailView):
    model = ShoppingCart
    template_name = 'shop/shoppingcart/detail.html'
    context_object_name = 'shopping_cart'

class ShoppingCartUpdateView(UpdateView):
    model = ShoppingCart
    template_name = 'shop/shoppingcart/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_shopping_cart')

class ShoppingCartDeleteView(DeleteView):
    model = ShoppingCart
    template_name = 'shop/shoppingcart/confirm_delete.html'
    success_url = reverse_lazy('shop_shopping_cart')
