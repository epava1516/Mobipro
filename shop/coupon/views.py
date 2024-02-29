from django.views.generic import TemplateView
from shop.coupon.models import Coupon

class CouponListView(TemplateView):
    template_name = 'shop/coupon_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coupons = Coupon.objects.all()

        # Filtrar por código si se proporciona en la consulta
        code = self.request.GET.get('code')
        if code:
            coupons = coupons.filter(code__icontains=code)

        # Aplicar paginación
        from django.core.paginator import Paginator
        paginator = Paginator(coupons, 10)  # Mostrar 10 cupones por página
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['coupons'] = page_obj
        return context
