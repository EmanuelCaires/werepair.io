from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
import debug_toolbar
from . import views
from .views import (
    ProductDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    ProductListView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('payment/success/', TemplateView.as_view(template_name='payment_success.html'), name='payment-success'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('phones/', views.phones, name='phones'),
    path('cases/', views.cases, name='cases'),
    path('replacement-parts/', views.replacement_parts, name='replacement-parts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('debug/', include('debug_toolbar.urls', namespace='debug_toolbar')),
    path('admin/', admin.site.urls),
]
