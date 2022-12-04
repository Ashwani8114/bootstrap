from django.db import models
from django.contrib.auth .models import User
from django.core.validators import MaxValueValidator , MinValueValidator

STATE_CHOICE = (
    
    ('Andhra Pradesh' , ('Andhra Pradesh')),
    ('Arunachal Pradesh' , ('Arunachal Pradesh')),
    ('Assam' , ('Assam')),
    ('Bihar' , ('Bihar')),
    ('Chhattisgarh' , ('Chhattisgarh')),
    ('Goa' , ('Goa')),
    ('Gujarat' , ('Gujarat')),
    ('Haryana' , ('Haryana')),
    ('	Himachal Pradesh' , ('	Himachal Pradesh')),
    ('Jharkhand' , ('Jharkhand')),
    ('Karnataka' , ('Karnataka')),
    ('Kerala' , ('Kerala')),
    ('Madhya Pradesh' , ('Madhya Pradesh')),
    ('Maharashtra' , ('Maharashtra')),
    ('Manipur' , ('Manipur')),
    ('Meghalaya' , ('Meghalaya')),
    ('Mizoram' , ('Mizoram')),
    ('Nagaland' , ('Nagaland')),
    ('Odisha' , ('Odisha')),
    ('Punjab' , ('Punjab')),
    ('Rajasthan' , ('Rajasthan')),
    ('Sikkim' , ('Sikkim')),
    ('Tamil Nadu' , ('Tamil Nadu')),
    ('Telangana' , ('Telangana')),
    ('Tripura' , ('Tripura')),
    ('Uttar Pradesh' , ('Uttar Pradesh')),
    ('Uttarakhand' , ('Uttarakhand')),
    ('West Bengal' , ('West Bengal')),
    

)

class Customer(models.Model): 
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    locality = models.CharField(max_length=200)
    city  = models.CharField(max_length = 200)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICE , max_length=50)

    def __str__(self): 
        return str(self.id)


CATEGORY_CHOICE = (
    ('E' , 'Electric'),
    ('C' , 'Casmetics'),
    ('TW' , 'topwear'),
    ('BW' , 'bottomwear'),
    ('M' , 'mobile'),
    ('L' , 'laptop'),
)  


class Product(models.Model): 
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    disounted_price = models.FloatField()
    description = models.TextField()
    beand = models.CharField(max_length = 100)
    category = models.CharField(choices = CATEGORY_CHOICE  , max_length = 2)
    product_image = models.ImageField(upload_to = 'productimg')


    def __str__(self): 
        return str(self.id)

class Cart(models.Model) : 
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default  = 1) 


    def __str__(self): 
        return str(self.id) 

    @property
    def total_cost(self) :         
        return self.quantity * self.product.disounted_price





STATUS_CHOICE = ( 
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On the way' , 'On the way'),
    ('Delivered' , 'Delivered'),
    ('Cancel' , 'Cancel')
)

class OrderPlace(models.Model): 
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete = models.CASCADE) 
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    order_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50 , choices = STATUS_CHOICE , default = 'pending')


    def __str__(self): 
        return str(self.id)

# Create your models here.