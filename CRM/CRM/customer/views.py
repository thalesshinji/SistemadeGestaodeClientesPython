from django.shortcuts import render
from django.views.generic import ListView
from .models import customer
class CustomerListView(ListView) :
    template_name = "customer/customer_list.html"
    model = customer
    queryset = customer.objects.all()

# Create your views here.
 