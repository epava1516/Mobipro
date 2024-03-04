from django.urls import path
from kernel.views import AdminMainPageView, ShopMainPageView
from shop.auditlog.views import AuditLogListView, auditlog_filtered
from shop.comment.views import (
    CommentListView, 
    CommentCreateView, 
    CommentDetailView, 
    CommentUpdateView, 
    CommentDeleteView
)
from shop.category.views import (
    CategoryListView, 
    CategoryCreateView, 
    CategoryDetailView, 
    CategoryUpdateView, 
    CategoryDeleteView,
    category_filtered,
)
from shop.coupon.views import (
    CouponListView, 
    CouponCreateView, 
    CouponDetailView, 
    CouponUpdateView, 
    CouponDeleteView
)
from shop.gallery.views import (
    GalleryListView, 
    GalleryCreateView, 
    GalleryDetailView, 
    GalleryUpdateView, 
    GalleryDeleteView
)
from shop.order.views import (
    OrderListView, 
    OrderCreateView, 
    OrderDetailView, 
    OrderUpdateView, 
    OrderDeleteView
)
from shop.product.views import (
    ProductListView, 
    ProductCreateView, 
    ProductDetailView, 
    ProductUpdateView, 
    ProductDeleteView
)
from shop.promotion.views import (
    PromotionListView, 
    PromotionCreateView, 
    PromotionDetailView, 
    PromotionUpdateView, 
    PromotionDeleteView
)
from shop.rating.views import (
    RatingListView, 
    RatingCreateView, 
    RatingDetailView, 
    RatingUpdateView, 
    RatingDeleteView
)
from shop.returnrefund.views import (
    ReturnRefundListView, 
    ReturnRefundCreateView, 
    ReturnRefundDetailView, 
    ReturnRefundUpdateView, 
    ReturnRefundDeleteView
)
from shop.shipping.views import (
    ShippingListView, 
    ShippingCreateView, 
    ShippingDetailView, 
    ShippingUpdateView, 
    ShippingDeleteView
)
from shop.shoppingcart.views import (
    ShoppingCartListView, 
    ShoppingCartCreateView, 
    ShoppingCartDetailView, 
    ShoppingCartUpdateView, 
    ShoppingCartDeleteView
)
from shop.tag.views import (
    TagListView, 
    TagCreateView, 
    TagDetailView, 
    TagUpdateView, 
    TagDeleteView
)

from shop.useractivity.views import (
    UserActivityListView,
    UserActivityCreateView,
    UserActivityDetailView,
    UserActivityUpdateView,
    UserActivityDeleteView
)

from kernel.views import load_users, load_products, load_actions, load_models, load_order_number

urlpatterns = [
    path('admin/', AdminMainPageView.as_view(), name='shop_main_page'),
    path('admin/shop/', ShopMainPageView.as_view(), name='shop_main_page'),
]

shop_urls = [
    # Audit-Log
    path('admin/shop/audit-log/', AuditLogListView.as_view(), name='shop_audit_log'),

    # Categories CRUD
    path('admin/shop/categories/', CategoryListView.as_view(), name='shop_categories'),
    path('admin/shop/categories/add/', CategoryCreateView.as_view(), name='shop_categories_add'),
    path('admin/shop/categories/detail/', CategoryDetailView.as_view(), name='shop_categories_detail'),
    path('admin/shop/categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='shop_categories_edit'),
    path('admin/shop/categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='shop_categories_delete'),

    # Comments CRUD
    path('admin/shop/comments/', CommentListView.as_view(), name='shop_comments'),
    path('admin/shop/comments/add/', CommentCreateView.as_view(), name='shop_comments_add'),
    path('admin/shop/comments/detail/', CommentDetailView.as_view(), name='shop_comments_detail'),
    path('admin/shop/comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='shop_comments_edit'),
    path('admin/shop/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='shop_comments_delete'),

    # Coupons CRUD
    path('admin/shop/coupons/', CouponListView.as_view(), name='shop_coupons'),
    path('admin/shop/coupons/add/', CouponCreateView.as_view(), name='shop_coupons_add'),
    path('admin/shop/coupons/detail/', CouponDetailView.as_view(), name='shop_coupons_detail'),
    path('admin/shop/coupons/<int:pk>/edit/', CouponUpdateView.as_view(), name='shop_coupons_edit'),
    path('admin/shop/coupons/<int:pk>/delete/', CouponDeleteView.as_view(), name='shop_coupons_delete'),

    # Gallery CRUD
    path('admin/shop/gallery/', GalleryListView.as_view(), name='shop_gallery'),
    path('admin/shop/gallery/add/', GalleryCreateView.as_view(), name='shop_gallery_add'),
    path('admin/shop/gallery/detail/', GalleryDetailView.as_view(), name='shop_gallery_detail'),
    path('admin/shop/gallery/<int:pk>/edit/', GalleryUpdateView.as_view(), name='shop_gallery_edit'),
    path('admin/shop/gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='shop_gallery_delete'),

    # Orders CRUD
    path('admin/shop/orders/', OrderListView.as_view(), name='shop_orders'),
    path('admin/shop/orders/add/', OrderCreateView.as_view(), name='shop_orders_add'),
    path('admin/shop/orders/detail/', OrderDetailView.as_view(), name='shop_orders_detail'),
    path('admin/shop/orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='shop_orders_edit'),
    path('admin/shop/orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='shop_orders_delete'),

    # Products CRUD
    path('admin/shop/products/', ProductListView.as_view(), name='shop_products'),
    path('admin/shop/products/add/', ProductCreateView.as_view(), name='shop_products_add'),
    path('admin/shop/products/detail/', ProductDetailView.as_view(), name='shop_products_detail'),
    path('admin/shop/products/<int:pk>/edit/', ProductUpdateView.as_view(), name='shop_products_edit'),
    path('admin/shop/products/<int:pk>/delete/', ProductDeleteView.as_view(), name='shop_products_delete'),

    # Promotion CRUD
    path('admin/shop/promotions/', PromotionListView.as_view(), name='shop_promotions'),
    path('admin/shop/promotions/add/', PromotionCreateView.as_view(), name='shop_promotions_add'),
    path('admin/shop/promotions/detail/', PromotionDetailView.as_view(), name='shop_promotions_detail'),
    path('admin/shop/promotions/<int:pk>/edit/', PromotionUpdateView.as_view(), name='shop_promotions_edit'),
    path('admin/shop/promotions/<int:pk>/delete/', PromotionDeleteView.as_view(), name='shop_promotions_delete'),

    # Ratings CRUD
    path('admin/shop/ratings/', RatingListView.as_view(), name='shop_ratings'),
    path('admin/shop/ratings/add/', RatingCreateView.as_view(), name='shop_ratings_add'),
    path('admin/shop/ratings/detail/', RatingDetailView.as_view(), name='shop_ratings_detail'),
    path('admin/shop/ratings/<int:pk>/edit/', RatingUpdateView.as_view(), name='shop_ratings_edit'),
    path('admin/shop/ratings/<int:pk>/delete/', RatingDeleteView.as_view(), name='shop_ratings_delete'),

    # Return / Refund CRUD
    path('admin/shop/returns/', ReturnRefundListView.as_view(), name='shop_returns'),
    path('admin/shop/returns/add/', ReturnRefundCreateView.as_view(), name='shop_returns_add'),
    path('admin/shop/returns/detail/', ReturnRefundDetailView.as_view(), name='shop_returns_detail'),
    path('admin/shop/returns/<int:pk>/edit/', ReturnRefundUpdateView.as_view(), name='shop_returns_edit'),
    path('admin/shop/returns/<int:pk>/delete/', ReturnRefundDeleteView.as_view(), name='shop_returns_delete'),

    # Shipping CRUD
    path('admin/shop/shipping/', ShippingListView.as_view(), name='shop_shipping'),
    path('admin/shop/shipping/add/', ShippingCreateView.as_view(), name='shop_shipping_add'),
    path('admin/shop/shipping/detail/', ShippingDetailView.as_view(), name='shop_shipping_detail'),
    path('admin/shop/shipping/<int:pk>/edit/', ShippingUpdateView.as_view(), name='shop_shipping_edit'),
    path('admin/shop/shipping/<int:pk>/delete/', ShippingDeleteView.as_view(), name='shop_shipping_delete'),

    # Shopping Cart CRUD
    path('admin/shop/shopping-cart/', ShoppingCartListView.as_view(), name='shop_shopping_cart'),
    path('admin/shop/shopping-cart/add/', ShoppingCartCreateView.as_view(), name='shop_shopping_cart_add'),
    path('admin/shop/shopping-cart/detail/', ShoppingCartDetailView.as_view(), name='shop_shopping_cart_detail'),
    path('admin/shop/shopping-cart/<int:pk>/edit/', ShoppingCartUpdateView.as_view(), name='shop_shopping_cart_edit'),
    path('admin/shop/shopping-cart/<int:pk>/delete/', ShoppingCartDeleteView.as_view(), name='shop_shopping_cart_delete'),

    # Tags CRUD
    path('admin/shop/tags/', TagListView.as_view(), name='shop_tags'),
    path('admin/shop/tags/add/', TagCreateView.as_view(), name='shop_tags_add'),
    path('admin/shop/tags/detail/', TagDetailView.as_view(), name='shop_tags_detail'),
    path('admin/shop/tags/<int:pk>/edit/', TagUpdateView.as_view(), name='shop_tags_edit'),
    path('admin/shop/tags/<int:pk>/delete/', TagDeleteView.as_view(), name='shop_tags_delete'),

    # UserActivity CRUD
    path('admin/shop/user-activity/', UserActivityListView.as_view(), name='shop_user_activity'),
    path('admin/shop/user-activity/add/', UserActivityCreateView.as_view(), name='shop_user_activity_add'),
    path('admin/shop/user-activity/<int:pk>/', UserActivityDetailView.as_view(), name='shop_user_activity_detail'),
    path('admin/shop/user-activity/<int:pk>/edit/', UserActivityUpdateView.as_view(), name='shop_user_activity_edit'),
    path('admin/shop/user-activity/<int:pk>/delete/', UserActivityDeleteView.as_view(), name='shop_user_activity_delete'),
]

urlpatterns += shop_urls


json_urls = [
    path('category-filtered', category_filtered, name='category_filtered'),
    path('auditlog-filtered/', auditlog_filtered, name='auditlog_filtered'),
    path('load-users/', load_users, name='load_users'),
    path('load-models/', load_models, name='load_models'),
    path('load-actions/', load_actions, name='load_actions'),
    path('load-products/', load_products, name='load_products'),
    path('load-order-number/', load_order_number, name='load_order_number'),
]

urlpatterns += json_urls