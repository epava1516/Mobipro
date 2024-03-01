from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.promotion.models import Promotion

class PromotionListView(ListView):
    model = Promotion
    template_name = 'shop/promotion/list.html'
    context_object_name = 'promotions'

class PromotionCreateView(CreateView):
    model = Promotion
    template_name = 'shop/promotion/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_promotions')

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'shop/promotion/detail.html'
    context_object_name = 'promotion'

class PromotionUpdateView(UpdateView):
    model = Promotion
    template_name = 'shop/promotion/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_promotions')

class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'shop/promotion/confirm_delete.html'
    success_url = reverse_lazy('shop_promotions')
