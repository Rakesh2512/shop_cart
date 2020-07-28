from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides = n//4+ ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # all =[[products,range(1,nSlides),nSlides],
    # [products,range(1,nSlides),nSlides]]
    all = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        all.append([prod, range(1, nSlides), nSlides])

    params = {'all': all}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def Tracker(request):
    return render(request, 'shop/tracker.html')


def ProductView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})


def CheckOut(request):
    return render(request, 'shop/checkout.html')
