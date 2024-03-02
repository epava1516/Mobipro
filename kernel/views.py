from django.views.generic import TemplateView
from shop.product.models import Product
from shop.auditlog.models import AuditLog
from django.http import JsonResponse
from django.contrib.auth.models import User

class AdminMainPageView(TemplateView):
    template_name = 'admin/main.html'

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