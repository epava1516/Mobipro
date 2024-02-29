from django.views.generic import TemplateView
from shop.gallery.models import Gallery

class GalleryListView(TemplateView):
    template_name = 'shop/gallery_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        return context
