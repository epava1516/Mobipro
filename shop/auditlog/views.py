from django.views.generic import TemplateView
from shop.auditlog.forms import AuditLogFilterForm
from shop.auditlog.models import AuditLog

class AuditLogListView(TemplateView):
    template_name = 'shop/auditlog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = AuditLogFilterForm(self.request.GET)
        context['form'] = form

        # Filtrar los registros de Audit Log según los datos del formulario
        queryset = AuditLog.objects.all()

        if form.is_valid():
            model_name = form.cleaned_data.get('model_name')
            if model_name:
                queryset = queryset.filter(model_name=model_name)
            action = form.cleaned_data.get('action')
            if action:
                queryset = queryset.filter(action=action)
            user = form.cleaned_data.get('user')
            if user:
                queryset = queryset.filter(user__username__icontains=user)
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            if start_date and end_date:
                queryset = queryset.filter(timestamp__range=(start_date, end_date))
            order_by = form.cleaned_data.get('order_by')
            if order_by:
                queryset = queryset.order_by(order_by)

        context['audit_logs'] = queryset
        return context