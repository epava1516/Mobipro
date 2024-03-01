from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shop.rating.models import Rating

class RatingListView(ListView):
    model = Rating
    template_name = 'shop/rating/list.html'
    context_object_name = 'ratings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['show_add_button'] = True # Muestra el botón de agregar
        # context['add_url_variable'] = reverse_lazy('shop_coupons_add') # URL de la vista de agregar
        context['shop_title'] = 'Calificaciones'
        context['title'] = 'Rating'
        return context

class RatingCreateView(CreateView):
    model = Rating
    template_name = 'shop/rating/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_ratings')

class RatingDetailView(DetailView):
    model = Rating
    template_name = 'shop/rating/detail.html'
    context_object_name = 'rating'

class RatingUpdateView(UpdateView):
    model = Rating
    template_name = 'shop/rating/form.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_ratings')

class RatingDeleteView(DeleteView):
    model = Rating
    template_name = 'shop/rating/confirm_delet-e.html'
    success_url = reverse_lazy('shop_ratings')