from django.views.generic import TemplateView
from shop.product.models import Product
from shop.category.models import Category
from shop.auditlog.models import AuditLog
from shop.order.models import Order
from django.http import JsonResponse
from django.contrib.auth.models import User

class AdminMainPageView(TemplateView):
    template_name = 'admin/main.html'

class ShopMainPageView(TemplateView):
    template_name = 'shop/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calcula el número total de categorías
        total_categories = Category.objects.count()
        
        # Calcula el número de categorías activas e inactivas
        active_categories = Category.objects.filter(is_active=True).count()
        inactive_categories = total_categories - active_categories
        
        # Calcula el porcentaje de categorías activas e inactivas
        if total_categories > 0:
            active_percentage = (active_categories / total_categories) * 100
            inactive_percentage = (inactive_categories / total_categories) * 100
        else:
            active_percentage = 0
            inactive_percentage = 0
        
        # Añade los datos al contexto
        context['total_categories'] = total_categories
        context['active_percentage'] = round(active_percentage, 2)
        context['inactive_percentage'] = round(inactive_percentage, 2)
        context['active_categories'] = active_categories
        context['inactive_categories'] = inactive_categories
        
        return context


# Funciones JSON
def load_users(request):
    users = User.objects.all().values('id', 'username')
    return JsonResponse({'users': list(users)})

def load_products(request):
    products = Product.objects.all().values('id', 'name')
    return JsonResponse({'products': list(products)})

def load_models(request):
    models = AuditLog.objects.values_list('model_name', flat=True).distinct()
    return JsonResponse({'models': list(models)})

def load_actions(request):
    actions = AuditLog.objects.values_list('action', flat=True).distinct()
    return JsonResponse({'actions': list(actions)})

def load_order_number(request):
    order_numbers = Order.objects.values_list('order_number', flat=True).distinct()
    return JsonResponse({'order_numbers': list(order_numbers)})
