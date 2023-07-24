from django.shortcuts import render, redirect
from . models import contact, Product
from django.contrib import messages
from math import ceil
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        allproduct = []
        catproduct = Product.objects.values('catagory', 'id')
        cats = {item['catagory'] for item in catproduct}
        for cat in cats:
            prod = Product.objects.filter(catagory = cat)
            n = len(prod)
            nSlider = n // 4 + ceil((n/4) - (n // 4))
            allproduct.append([prod ,(1,nSlider), nSlider])
        parms = {'allproduct' : allproduct}
        return render(request,'index.html',parms)
    return redirect('login')

def is_match(item,query):
    if query in item.product_name or query in item.catagory or query in item.dese:
        return True
    return False

def search(request):
    query = request.GET.get('Search')
    if request.user.is_authenticated:
        allproduct = []
        catproducts = Product.objects.values('catagory', 'id')
        # cats = [ item['catagory'] for item in catproducts ]
        cats = {item['catagory'] for item in  catproducts}
        for cat in cats:
            prodtamp = Product.objects.filter(catagory = cat)
            prod = [item for item in prodtamp if is_match(item, query)]
            n = len(prod)
            nSlider = n // 4 + ceil((n/4) - (n // 4))
            allproduct.append([prod ,(1,nSlider), nSlider])
        parms = {'allproduct' : allproduct}
        return render(request,'index.html',parms)
    return redirect('login')


def contac(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Name = request.POST.get('Name')
            email = request.POST.get('email')
            Pnumber = request.POST.get('pnumber')
            dese = request.POST.get('dese')
            mycontact = contact(email=email,Name=Name, Phone_number = Pnumber, dese= dese)
            mycontact.save()
            messages.success(request,"Your Responce has been recoted")   
            messages.success(request,"We will contac you")   
        return render(request,'contac.html')
    return redirect('login')


def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html')
    return redirect('login')