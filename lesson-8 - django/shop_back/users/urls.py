from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/register/', RegisterView.as_view(), name='api_register'),
]