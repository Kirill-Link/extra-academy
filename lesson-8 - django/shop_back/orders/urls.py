from django.urls import path, include

from rest_framework import routers
from . import views
from .views import BuyProductView, UserOrderViewSet

router = routers.DefaultRouter()
router.register(r'order', views.OrderList)
router.register(r'order-item', views.OrderItemList)
router.register(r'user/(?P<user_id>\d+)/orders', UserOrderViewSet, basename='user-orders')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product_id>/buy/', BuyProductView.as_view(), name='buy-product')
]

