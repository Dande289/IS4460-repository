from django.urls import path
from .views import CustomerListCreateView, CustomerListDetailView
urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerListDetailView.as_view(), name='customer-list-detail'),
]