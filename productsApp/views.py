from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request,'productsApp/productlist.html')