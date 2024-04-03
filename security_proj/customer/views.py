from django.shortcuts import render
from django.views import View
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import CustomerSerializer
from rest_framework import generics

# Create your views here.
def can_view_cust(request):
    return request.user.groups.filter(name = 'Can View Customers').exists()


class CustomerListView(LoginRequiredMixin,View):

    def get(self,request):

        user_message = ""
        customers = None

        if not can_view_cust(request):
            user_message = "Cannot View Customers. Not in 'Can View Customers' Group!"
        else:
            customers = Customer.objects.all()
        
        return render(request=request,
                      template_name='customer/customer_list.html',
                      context = {'customers':customers,'user_message':user_message}
                      )
    

class CustomerListCreateView(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer