from django.views.generic import TemplateView
from django.utils.timezone import make_aware
from datetime import datetime
from shop.rating.models import Rating

class RatingListView(TemplateView):
    template_name = 'shop/rating_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener parámetros de filtro
        user = self.request.GET.get('user')
        product = self.request.GET.get('product')
        value = self.request.GET.get('value')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        # Filtrar clasificaciones
        ratings = Rating.objects.all()
        if user:
            ratings = ratings.filter(user__username__icontains=user)
        if product:
            ratings = ratings.filter(product__name__icontains=product)
        if value:
            ratings = ratings.filter(value=value)
        if start_date:
            start_date = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
            ratings = ratings.filter(created_at__gte=start_date)
        if end_date:
            end_date = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
            ratings = ratings.filter(created_at__lte=end_date)
        
        context['ratings'] = ratings
        return context
