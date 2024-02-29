from django.views.generic import TemplateView
from shop.order.models import Order

class OrderListView(TemplateView):
    template_name = 'shop/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()

        # Filtrar por usuario si se proporciona en la solicitud
        user = self.request.GET.get('user')
        if user:
            orders = orders.filter(user__username__icontains=user)

        # Filtrar por estado si se proporciona en la solicitud
        status = self.request.GET.get('status')
        if status:
            orders = orders.filter(status=status)

        # Filtrar por rango de fechas si se proporciona en la solicitud
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date and end_date:
            orders = orders.filter(created_at__range=[start_date, end_date])

        context['orders'] = orders
        return context
