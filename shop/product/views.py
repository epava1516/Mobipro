from django.views.generic import TemplateView
from shop.product.models import Product

class ProductListView(TemplateView):
    template_name = 'shop/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
