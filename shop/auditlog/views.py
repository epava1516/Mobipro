from django.views.generic import ListView
from shop.auditlog.models import AuditLog
from django.http import JsonResponse
from django.template.loader import render_to_string

def auditlog_filtered(request):
    # Obtener los parámetros de filtrado de la solicitud GET
    model_name = request.GET.get('model_name')
    action = request.GET.get('action')
    user = request.GET.get('user')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Filtrar los registros de auditlog
    queryset = AuditLog.objects.all()
    if model_name:
        queryset = queryset.filter(model_name=model_name)
    if action:
        queryset = queryset.filter(action=action)
    if user:
        queryset = queryset.filter(user__username=user)
    if start_date:
        queryset = queryset.filter(timestamp__gte=start_date)
    if end_date:
        queryset = queryset.filter(timestamp__lte=end_date)

    # Renderizar la tabla y devolverla como respuesta JSON
    html = render_to_string('shop/auditlog/table.html', {'audit_logs': queryset})
    return JsonResponse({'html': html})


class AuditLogListView(ListView):
    template_name = 'shop/auditlog/list.html'
    model = AuditLog
    context_object_name = 'audit_logs'
    paginate_by = 10

    def get_queryset(self):
        # Obtener los parámetros de la solicitud GET
        model_name = self.request.GET.get('model_name')
        action = self.request.GET.get('action')
        user = self.request.GET.get('user')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        # Filtrar los registros de acuerdo a los parámetros recibidos
        queryset = super().get_queryset()
        if model_name:
            queryset = queryset.filter(model_name=model_name)
        if action:
            queryset = queryset.filter(action=action)
        if user:
            queryset = queryset.filter(user__username=user)
        if start_date:
            queryset = queryset.filter(timestamp__gte=start_date)
        if end_date:
            queryset = queryset.filter(timestamp__lte=end_date)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = list(set(AuditLog.objects.values_list('model_name', flat=True)))
        context['action_list'] = list(set(AuditLog.objects.values_list('action', flat=True)))
        context['user_list'] = list(set(AuditLog.objects.values_list('user', flat=True)))
        return context
