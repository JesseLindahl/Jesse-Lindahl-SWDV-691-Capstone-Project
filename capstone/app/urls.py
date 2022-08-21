from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main, name="main"),
    path('index/', views.index, name="index"),
    
    path('account/', views.account, name="account"),
    path('cancel/', views.cancel, name="cancel"),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('product/', views.product, name="product"),
    path('store/', views.store, name="store"),
    path('success/', views.success, name="success"),
    path('workout/', views.workout, name="workout"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]