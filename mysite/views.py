from django.shortcuts import render


def index(request):
    return render(request, 'mysite/base.html')

def info(request):
    return render(request, 'mysite/info.html')

def kontakt(request):
    return render(request, 'mysite/kontakt.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

def price(request):
    return render(request, 'mysite/price.html')

def poslug(request):
    return render(request, 'mysite/poslug.html')
