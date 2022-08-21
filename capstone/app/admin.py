from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItems)
admin.site.register(ShippingAddress)
admin.site.register(ContactForm)
admin.site.register(Blog)
admin.site.register(Blogs)
admin.site.register(Post)