from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.coupon.models import Coupon

class CouponListView(ListView):
    model = Coupon
    template_name = 'shop/coupon/list.html'
    context_object_name = 'coupons'

class CouponCreateView(CreateView):
    model = Coupon
    template_name = 'shop/coupon/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_coupons')

class CouponDetailView(DetailView):
    model = Coupon
    template_name = 'shop/coupon/detail.html'
    context_object_name = 'coupon'

class CouponUpdateView(UpdateView):
    model = Coupon
    template_name = 'shop/coupon/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_coupons')

class CouponDeleteView(DeleteView):
    model = Coupon
    template_name = 'shop/coupon/confirm_delete.html'
    success_url = reverse_lazy('shop_coupons')
