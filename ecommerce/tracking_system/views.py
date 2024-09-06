from django.shortcuts import render
from . import order
# Create your views here.

def orders(request):
    print(order.order.getAllOrders())
    return render(request,'tracking_system/orders.html',{'orderlist':order.order.getAllOrders()})