from django.shortcuts import render,redirect
from .models import Account
from .forms import CustomAccountCreateForm,CustomAccountChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def form(request):
    if request.method == 'GET':
        form = CustomAccountCreateForm()
        return render(request, 'userApp/index.html', {'form': form})
    else:
        form = CustomAccountCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/user/login')

def signin(request):
    if request.method == 'GET':
        return render(request, 'userApp/login.html')
    else:
        username =request.POST['username']
        password = request.POST['password']

        user = authenticate(username= username, password= password)
        if user is not None:
            print('Valid login')
            login(request, user)
            return render(request, 'productsApp/productlist.html')
        else:
            messages.error(request,'Bad credentials')
            return render(request,'userApp/login.html')



