from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *

# Create your views here.

def main(request):
    #Needed for data to be passed through 
    context = {}
    return render(request, 'app/main.html', context)

def index(request):
    # Populates all the blog posts currently stored in the database
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'app/index.html', context)

def postDetails(request, slug):
    post = Post.objects.get(slug = slug)
    context = {'post':post}
    return render(request, 'app/post_detail.html', context)

def account(request):
    context = {}
    return render(request, 'app/account.html', context)
    
def cancel(request):
    context = {}
    return render(request, 'app/cancel.html', context)

def cart(request):

    #Needed to ensure the proper traits are being passed thourgh for order creation
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitems_set.all()
    else: 
        items = []
        order = {'order_total':0, 'cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'app/cart.html', context)

def contact(request):
    if request.method == "POST":
        contact = ContactForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        
    context = {}
    return render(request, 'app/contact.html', context)

def product(request):
    context = {}
    return render(request, 'app/product.html', context)

def store(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'app/store.html', context)

def success(request):
    context = {}
    return render(request, 'app/success.html', context)

def workout(request):
    context = {}
    return render(request, 'app/workout.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitems_set.all()
    else: 
        items = []
        order = {'order_total':0, 'cart_items':0}

    context = {'items' : items, 'order' : order}
    return render(request, 'app/checkout.html', context)
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:', productId)
    print('action:', action)
    customer = request.user.customer
    product = Products.objects.get(id = productId)

    #Logic for order creation 
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    #Updates order item quantity 
    orderItem, created = OrderItems.objects.get_or_create(order = order, product = product)
    if action == 'add': 
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    #Deletes an order
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item Updated', safe = False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data ['form'] ['total'])
        order.transaction_id = transaction_id

        if total == order.order_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    return JsonResponse('Order Confirmed', safe = False)