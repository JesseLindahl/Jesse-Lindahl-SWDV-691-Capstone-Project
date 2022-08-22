from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

# ERROR
class Product(models.Model):
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null = True, blank = False)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = True)
    transaction_id = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        orderitems = self.orderitems_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
            return shipping


    # Method for calculating order total
    @property
    def order_total(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def cart_items(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.quantity for item in orderitems])
        return total  

# ERROR
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True)
    city = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 200, null = True)
    zipcode = models.CharField(max_length = 200, null = True)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.address

class Products(models.Model):
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null = True, blank = False)
    image = models.ImageField(null = True, blank = True)
    def __str__(self):
        return self.name

class OrderItems(models.Model):
    product = models.ForeignKey(Products, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

# ERROR
class Blog(models.Model):
    subject = models.CharField(max_length = 200)
    post = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    # subclass that sets the blog posts in chronological order
    class PostOrder:
        post_order = ['-date_added']

# ERROR
class Blogs(models.Model):
    subject = models.CharField(max_length = 200)
    slug = models.SlugField()
    post = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    # subclass that sets the blog posts in chronological order
    class PostOrder:
        post_order = ['-date_added']

class Post(models.Model):
    subject = models.CharField(max_length = 200)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    # subclass that sets the blog posts in chronological order
    class PostOrder:
        post_order = ['-date_added']
