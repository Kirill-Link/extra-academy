from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryList)
router.register(r'products', views.ProductList)
router.register(r'category/(?P<category_id>\d+)/products', views.CategoryProductView, basename='category-products')


urlpatterns = [
    path('', include(router.urls)),
]