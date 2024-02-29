from django.views.generic import TemplateView
from shop.promotion.models import Promotion

class PromotionListView(TemplateView):
    template_name = 'shop/promotion_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promotions'] = Promotion.objects.all()
        return context
