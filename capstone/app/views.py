from django.shortcuts import render

# Create your views here.

def main(request):
    #Needed for data to be passed through 
    context = {}
    return render(request, 'app/main.html', context)

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def account(request):
    context = {}
    return render(request, 'app/account.html', context)
    
def cancel(request):
    context = {}
    return render(request, 'app/cancel.html', context)

def cart(request):
    context = {}
    return render(request, 'app/cart.html', context)

def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)

def product(request):
    context = {}
    return render(request, 'app/product.html', context)

def store(request):
    context = {}
    return render(request, 'app/store.html', context)

def success(request):
    context = {}
    return render(request, 'app/success.html', context)

def workout(request):
    context = {}
    return render(request, 'app/workout.html', context)

def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)