from django.shortcuts import render, redirect
from . models import contact, Product
from django.contrib import messages
from math import ceil
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        allproduct = []
        catproduct = Product.objects.values('catagory', 'id')
        # print(catproduct)
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

def is_multimatch(item,catagory,product_name, maxprise, minprise):
    return ((catagory == None or catagory in item.catagory) and (product_name == None or product_name in item.product_name) and (item.prise < maxprise and item.prise > minprise))
   

def search(request):
    query = request.GET.get('Search')
    if request.user.is_authenticated:
        allproduct = []
        catproducts = Product.objects.values('catagory', 'id')
        # cats = [ item['catagory'] for item in catproducts ]
        cats = {item['catagory'] for item in  catproducts}
        for cat in cats:
            prodtamp = Product.objects.filter(catagory = cat)
            # prodtamp = prodtamp.filter(prise = 1200)
            prod = [item for item in prodtamp if is_match(item, query)]
            n = len(prod)
            nSlider = n // 4 + ceil((n/4) - (n // 4))
            allproduct.append([prod ,(1,nSlider), nSlider])
        parms = {'allproduct' : allproduct}
        return render(request,'index.html',parms)
    return redirect('login')


def multisearch(request):
    catagory = request.GET.get('catagory')
    product_name = request.GET.get('product_name')
    maxprise = request.GET.get('maxval')
    minprise = request.GET.get('minval')
    if maxprise == "":
        maxprise = 10000
    else: maxprise = int(maxprise)
    if minprise == "":
        minprise = 0
    else : minprise = int(minprise)
    print(type(maxprise), maxprise,product_name)
    if request.user.is_authenticated:
        allproduct = []
        catproducts = Product.objects.values('catagory', 'id')
        # cats = [ item['catagory'] for item in catproducts ]
        cats = {item['catagory'] for item in  catproducts}
        for cat in cats:
            prodtamp = Product.objects.filter(catagory = cat)
            # prodtamp = prodtamp.filter(prise = 1200)
            prod = [item for item in prodtamp if is_multimatch(item, catagory, product_name, maxprise, minprise)]
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

def chickout(request):
    return render(request,'chickout.html')