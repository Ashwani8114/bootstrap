from django.shortcuts import render , redirect , HttpResponse
from django.views import View
from .models import Customer , Product , Cart , OrderPlace 
from .forms import CustomerRegistraionForm  , CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View) : 
    def get(sself , request):
       topwear = Product.objects.filter(category = 'TW')
       bottomwear = Product.objects.filter(category = 'BW')
       electric = Product.objects.filter(category = 'E')
       casmetics = Product.objects.filter(category = 'C')

       return render(request , 'app/home.html' , {'topwear' : topwear , 'bottomwear' : bottomwear ,
                     'electric': electric , 'casmetics' : casmetics})

# def product_detail(request):
#   return render(request, 'app/productdetail.html')

class ProductDatailView(View):
    def get(self , request , pk): 
        product = Product.objects.get(pk=pk)
        return render(request , 'app/productdetail.html' , {'product' : product})



# by using cart which is used in django
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Cart(user = user , product = product).save()
    return redirect('/cart/')


def show_cart(request) : 
    if request.user.is_authenticated : 
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0.0
        shiping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product : 
            for p in cart_product :
                tempamount = (p.quantity * p.product. disounted_price)
                amount += tempamount
                totalamount = amount + shiping_amount 
        
       
            return render(request, 'app/addtocart.html' , {'carts' : cart ,
            'totalamount' : totalamount , 'amount' : amount})

        else : 
            return render(request , 'app/empatycart.html') 


# plus cart in quantity         
def plus_cart(request) : 
    if request.method == 'GET' :
        
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shiping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product :
            tempamount = (p.quantity * p.product. disounted_price)
            amount += tempamount
            # totalamount = amount + shiping_amount

        data = { 
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : amount + shiping_amount
        }

        return JsonResponse(data)



# minus cart in quantity 
def minus_cart(request) : 
    if request.method == 'GET' :
        
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shiping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product :
            tempamount = (p.quantity * p.product. disounted_price)
            amount += tempamount
            # totalamount = amount + shiping_amount

        data = { 
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : amount + shiping_amount
        }

        return JsonResponse(data)


# remove cart in quantity 
def remove_cart(request) : 
    if request.method == 'GET' :
        
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        
        c.delete()
        amount = 0.0
        shiping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product :
            tempamount = (p.quantity * p.product. disounted_price)
            amount += tempamount
            # totalamount = amount + shiping_amount

        data = { 
            
            'amount' : amount,
            'totalamount' : amount + shiping_amount
        }

        return JsonResponse(data)
        




def buy_now(request):
 return render(request, 'app/buynow.html')

# by using profile making views and class views 
class ProfileView(View) : 
    def get(self , request) : 
        form = CustomerProfileForm()
        return render(request , 'app/profile.html' , {'form' : form , 'active' : 'btn-dark'})

    def post(self , request) : 
        form = CustomerProfileForm(request.POST)   
        if form.is_valid() : 
            usr = request.user
            name = form.cleaned_data['name'] 
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
           

            reg = Customer(user = usr , name = name , locality = locality , city = city , state = state , 
            zipcode = zipcode)
            
            reg.save()
            messages.success(request , 'Congratulation !! profile updated Successfully ')
        
        return render(request , 'app/profile.html' , {'form' : form , 'active' : 'btn-dark'})


def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html' , {'add' : add , 'active' : 'btn-dark'})

def orders(request):
    op = OrderPlace.objects.filter(user = request.user)
    return render(request, 'app/orders.html' , {'order_place' : op})

# def change_password(request):
#  return render(request, 'app/changepassword.html')


# for using mobile in choice 

def mobile(request , data = None):
    if data == None: 
        mobile = Product.objects.filter(category = 'M')

    elif data == 'Redmi' or data == 'Samsung' or data == 'Vivo'or data == 'Oppo' or data == 'Realme' or data == 'Infinix' or data == 'iPhone' : 
        mobile = Product.objects.filter(category = 'M').filter(beand = data)

    elif data =='below' :
        mobile = Product.objects.filter(category = 'M').filter(disounted_price__lt = 10000)

    elif data == 'above' : 
        mobile = Product.objects.filter(category = 'M').filter(disounted_price__gt = 10000)      

    return render(request, 'app/mobile.html' , {'mobile' : mobile})


# Bottom wear in choice me 
def bottomwear(request , data = None):
    if data == None: 
        bottomwear = Product.objects.filter(category = 'BW')

    elif data == 'red Tap' or data == 'Zara' or data == 'Asian' or data == 'Peter england': 
        bottomwear = Product.objects.filter(category = 'BW').filter(beand = data)

    elif data =='below' :
        bottomwear = Product.objects.filter(category = 'BW').filter(disounted_price__lt = 1000)

    elif data == 'above' : 
        bottomwear = Product.objects.filter(category = 'BW').filter(disounted_price__gt = 1000)      

    return render(request, 'app/bottomwear.html' , {'bottomwear' : bottomwear})




# topwear in choice
def topwear(request , data = None):
    if data == None: 
        topwear = Product.objects.filter(category = 'TW')

    elif data == 'Manyawar' or data == 'van husain' or data == 'Zara' or data == 'Roadster' or data == 'Peter england': 
        topwear = Product.objects.filter(category = 'TW').filter(beand = data)

    elif data =='below' :
        topwear = Product.objects.filter(category = 'TW').filter(disounted_price__lt = 500)

    elif data == 'above' : 
        topwear = Product.objects.filter(category = 'TW').filter(disounted_price__gt = 500)      

    return render(request, 'app/topwear.html' , {'topwear' : topwear}) 






# for registration 
# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View) : 
    def get(self , request) : 
       form = CustomerRegistraionForm()
       return render(request , 'app/customerregistration.html' , {'form' : form})

    def post(self , request) : 
        form =  CustomerRegistraionForm(request.POST)
        if form.is_valid() :
            messages.success(request , 'congratulations!! Registered Successfully') 
            form.save()   
        return render(request , 'app/customerregistration.html' , {'form' : form})    

def password_resert(request) : 
    return render(request , 'password_resert.html')


def checkout(request):
    user = request.user
    add = Customer.objects.filter(user = user)
    cart_items = Cart.objects.filter(user = user)

    amount = 0.0
    shiping_amount = 70.0
    totalamount = 00.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product : 
       for p in cart_product :
            tempamount = (p.quantity * p.product. disounted_price)
            amount += tempamount
            totalamount = amount + shiping_amount

    return render(request, 'app/checkout.html' , {'add' : add , 'totalamount' : totalamount , 'cart_items' : cart_items})



def payment_done(request) : 
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id = custid)
    cart = Cart.objects.filter(user = user)
    for c in cart : 
        OrderPlace(user = user , customer = customer , product = c.product , quantity = c.quantity).save()
        c.delete()
    return redirect('/orders/')    