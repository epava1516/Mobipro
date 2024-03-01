from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.shipping.models import Shipping

class ShippingListView(ListView):
    model = Shipping
    template_name = 'shop/shipping/list.html'
    context_object_name = 'shippings'

class ShippingCreateView(CreateView):
    model = Shipping
    template_name = 'shop/shipping/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_shipping')

class ShippingDetailView(DetailView):
    model = Shipping
    template_name = 'shop/shipping/detail.html'
    context_object_name = 'shipping'

class ShippingUpdateView(UpdateView):
    model = Shipping
    template_name = 'shop/shipping/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_shipping')

class ShippingDeleteView(DeleteView):
    model = Shipping
    template_name = 'shop/shipping/confirm_delete.html'
    success_url = reverse_lazy('shop_shipping')
