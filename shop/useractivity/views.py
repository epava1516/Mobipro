from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.useractivity.models import UserActivity

class UserActivityListView(ListView):
    model = UserActivity
    template_name = 'shop/useractivity/list.html'
    context_object_name = 'user_activities'

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
