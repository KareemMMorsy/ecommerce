from django.shortcuts import render
from products.models import Product

# Create your views here.
def cart(request):
    allproducts=Product.objects.all()
    myprod=allproducts.filter(active=True)
    return render(request,'mart/cart.html',{'prodlist':myprod})