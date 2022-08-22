from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.main, name="main"),
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('workout/', views.workout, name="workout"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]