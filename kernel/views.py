from django.views.generic import TemplateView

class AdminMainPageView(TemplateView):
    template_name = 'admin/main.html'
