"""
URL configuration for kernel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
from django.urls import path
from kernel.views import AdminMainPageView

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    # Main Page
    path('admin/', AdminMainPageView.as_view(), name='shop_main_page'),
]

from shop.auditlog.views import AuditLogListView
from shop.comment.views import CommentListView
from shop.category.views import CategoryListView
from shop.coupon.views import CouponListView
from shop.gallery.views import GalleryListView
from shop.order.views import OrderListView
from shop.product.views import ProductListView
from shop.promotion.views import PromotionListView


shop_urls = [
    # Audit-Log
    path('admin/shop/audit-log/', AuditLogListView.as_view(), name='shop_audit_log'),

    # Categories CRUD
    path('admin/shop/categories/', CategoryListView.as_view(), name='shop_categories'),
    path('admin/shop/categories/add/', AdminMainPageView.as_view(), name='shop_categories_add'),
    path('admin/shop/categories/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_categories_edit'),
    path('admin/shop/categories/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_categories_delete'),

    # Comments CRUD
    path('admin/shop/comments/', CommentListView.as_view(), name='shop_comments'),
    path('admin/shop/comments/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_comments_edit'),
    path('admin/shop/comments/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_comments_delete'),

    # Coupons CRUD
    path('admin/shop/coupons/', CouponListView.as_view(), name='shop_coupons'),
    path('admin/shop/coupons/add/', AdminMainPageView.as_view(), name='shop_coupons_add'),
    path('admin/shop/coupons/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_coupons_edit'),
    path('admin/shop/coupons/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_coupons_delete'),

    # Gallery CRUD
    path('admin/shop/gallery/', GalleryListView.as_view(), name='shop_gallery'),
    path('admin/shop/gallery/add/', AdminMainPageView.as_view(), name='shop_gallery_add'),
    path('admin/shop/gallery/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_gallery_edit'),
    path('admin/shop/gallery/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_gallery_delete'),

    # Orders CRUD
    path('admin/shop/orders/', OrderListView.as_view(), name='shop_orders'),
    path('admin/shop/orders/add/', AdminMainPageView.as_view(), name='shop_orders_add'),
    path('admin/shop/orders/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_orders_edit'),

    # Products CRUD
    path('admin/shop/products/', ProductListView.as_view(), name='shop_products'),
    path('admin/shop/products/add/', AdminMainPageView.as_view(), name='shop_products_add'),
    path('admin/shop/products/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_products_edit'),
    path('admin/shop/products/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_products_delete'),

    # Promotion CRUD
    path('admin/shop/promotions/', PromotionListView.as_view(), name='shop_promotions'),
    path('admin/shop/promotions/add/', AdminMainPageView.as_view(), name='shop_promotions_add'),
    path('admin/shop/promotions/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_promotions_edit'),
    path('admin/shop/promotions/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_promotions_delete'),

    # Ratings CRUD
    path('admin/shop/ratings/', AdminMainPageView.as_view(), name='shop_ratings'),

    # Return / Refund CRUD
    path('admin/shop/returns/', AdminMainPageView.as_view(), name='shop_returns'),
    path('admin/shop/returns/add/', AdminMainPageView.as_view(), name='shop_returns_add'),
    path('admin/shop/returns/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_returns_edit'),
    path('admin/shop/returns/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_returns_delete'),

    # Shipping CRUD
    path('admin/shop/shipping/', AdminMainPageView.as_view(), name='shop_shipping'),
    path('admin/shop/shipping/add/', AdminMainPageView.as_view(), name='shop_shipping_add'),
    path('admin/shop/shipping/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_shipping_edit'),
    path('admin/shop/shipping/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_shipping_delete'),

    # Shopping Cart CRUD
    path('admin/shop/shopping-cart/', AdminMainPageView.as_view(), name='shop_shopping_cart'),
    path('admin/shop/shopping-cart/add/', AdminMainPageView.as_view(), name='shop_shopping_cart_add'),
    path('admin/shop/shopping-cart/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_shopping_cart_edit'),
    path('admin/shop/shopping-cart/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_shopping_cart_delete'),

    # Tags CRUD
    path('admin/shop/tags/', AdminMainPageView.as_view(), name='shop_tags'),
    path('admin/shop/tags/add/', AdminMainPageView.as_view(), name='shop_tags_add'),
    path('admin/shop/tags/edit/<int:id>/', AdminMainPageView.as_view(), name='shop_tags_edit'),
    path('admin/shop/tags/delete/<int:id>/', AdminMainPageView.as_view(), name='shop_tags_delete'),
]

urlpatterns += shop_urls