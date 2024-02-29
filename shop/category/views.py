from django.views.generic import TemplateView
from shop.category.models import Category

class CategoryListView(TemplateView):
    template_name = 'shop/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context