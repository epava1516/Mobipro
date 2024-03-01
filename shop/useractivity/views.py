from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.useractivity.models import UserActivity

class UserActivityListView(ListView):
    model = UserActivity
    template_name = 'shop/useractivity/list.html'
    context_object_name = 'user_activities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['show_add_button'] = True # Muestra el botón de agregar
        # context['add_url_variable'] = reverse_lazy('shop_coupons_add') # URL de la vista de agregar
        context['shop_title'] = 'Actividades de usuario'
        context['title'] = 'UserActivity'
        return context

class UserActivityCreateView(CreateView):
    model = UserActivity
    template_name = 'shop/useractivity/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_useractivities')

class UserActivityDetailView(DetailView):
    model = UserActivity
    template_name = 'shop/useractivity/detail.html'
    context_object_name = 'user_activity'

class UserActivityUpdateView(UpdateView):
    model = UserActivity
    template_name = 'shop/useractivity/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_useractivities')

class UserActivityDeleteView(DeleteView):
    model = UserActivity
    template_name = 'shop/useractivity/confirm_delete.html'
    success_url = reverse_lazy('shop_useractivities')
