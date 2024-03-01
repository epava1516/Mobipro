from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order

class OrderListView(ListView):
    model = Order
    template_name = 'shop/order/list.html'
    context_object_name = 'orders'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'shop/order/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_orders')

class OrderDetailView(DetailView):
    model = Order
    template_name = 'shop/order/detail.html'
    context_object_name = 'order'

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'shop/order/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_orders')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'shop/order/confirm_delete.html'
    success_url = reverse_lazy('shop_orders')
