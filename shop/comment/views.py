from django.views.generic import TemplateView
from shop.comment.models import Comment

class CommentListView(TemplateView):
    template_name = 'shop/comment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener todos los comentarios
        comments = Comment.objects.all()

        # Aplicar filtros si se proporcionan en la solicitud GET
        user = self.request.GET.get('user')
        if user:
            comments = comments.filter(user__username__icontains=user)

        product = self.request.GET.get('product')
        if product:
            comments = comments.filter(product__name__icontains=product)

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date and end_date:
            comments = comments.filter(created_at__range=(start_date, end_date))

        order_by = self.request.GET.get('order_by', '-created_at')
        comments = comments.order_by(order_by)

        context['comments'] = comments
        return context
