from django.urls import path
from .views import DelegateCreateAPIView

urlpatterns = [
    path('delegates/', DelegateCreateAPIView.as_view(), name='create-delegate'),
]
