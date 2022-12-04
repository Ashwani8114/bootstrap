from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlace
)

@admin.register(Customer)
class CustomerModleAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'name' , 'locality' , 'city' , 'zipcode' , 'state']

@admin.register(Product) 
class ProductModelAdmin(admin.ModelAdmin) : 
    list_display = ['id' , 'title' , 'selling_price' , 'disounted_price' ,
     'description' , 'beand' , 'category' ,'product_image']   


@admin.register(Cart) 
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'product' , 'quantity'] 

@admin.register(OrderPlace)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'customer' , 'product' , 'quantity' , 'order_date' , 'status']         


# Register your models here.
