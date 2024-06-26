from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView, OrderListCreateView, OrderDetailView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]