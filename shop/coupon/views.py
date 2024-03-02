from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.coupon.models import Coupon
from django.db.models import Q

class CouponListView(ListView):
    model = Coupon
    template_name = 'shop/coupon/list.html'
    context_object_name = 'coupons'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener parámetros de búsqueda
        search_query = self.request.GET.get('search', '')
        discount_percent = self.request.GET.get('discount_percent', None)
        start_date = self.request.GET.get('start_date', '')
        end_date = self.request.GET.get('end_date', '')
        is_active = self.request.GET.get('is_active', '')

        # Filtrar por código o descripción
        if search_query:
            queryset = queryset.filter(Q(code__icontains=search_query) | Q(description__icontains=search_query))

        # Filtrar por descuento
        if discount_percent:
            queryset = queryset.filter(discount_percent=discount_percent)

        # Filtrar por fecha de inicio
        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        # Filtrar por fecha de fin
        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)

        # Filtrar por estado
        if is_active != '':
            queryset = queryset.filter(is_active=is_active)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_add_button'] = True # Muestra el botón de agregar
        context['add_url_variable'] = reverse_lazy('shop_coupons_add') # URL de la vista de agregar
        context['shop_title'] = 'Cupones'
        context['title'] = 'Coupon'
        return context

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
