from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.returnrefund.models import ReturnRefund

class ReturnRefundListView(ListView):
    model = ReturnRefund
    template_name = 'shop/returnrefund/list.html'
    context_object_name = 'return_refunds'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['show_add_button'] = True # Muestra el botón de agregar
        # context['add_url_variable'] = reverse_lazy('shop_coupons_add') # URL de la vista de agregar
        context['shop_title'] = 'Devoluciones y Reembolsos'
        context['title'] = 'ReturnRefund'
        return context

class ReturnRefundCreateView(CreateView):
    model = ReturnRefund
    template_name = 'shop/returnrefund/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_returns')

class ReturnRefundDetailView(DetailView):
    model = ReturnRefund
    template_name = 'shop/returnrefund/detail.html'
    context_object_name = 'return_refund'

class ReturnRefundUpdateView(UpdateView):
    model = ReturnRefund
    template_name = 'shop/returnrefund/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_returns')

class ReturnRefundDeleteView(DeleteView):
    model = ReturnRefund
    template_name = 'shop/returnrefund/confirm_delete.html'
    success_url = reverse_lazy('shop_returns')
