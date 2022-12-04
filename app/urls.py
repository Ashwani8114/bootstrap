from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MyPassowrdChangeForm , MyPasswordResetForm , MySetPasswordForm

urlpatterns = [
# path('', views.home),
    path('' , views.ProductView.as_view(), name = 'home'),


# path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDatailView.as_view(), name='product-detail'),

# using cart which is used in django
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/' , views.show_cart , name = 'show_cart'),


# ajax code in django and increase and decrease 
    path('pluscart/' , views.plus_cart , name = 'plus_cart'),

# minus cart in quantity 
    path('minuscart/' , views.minus_cart , name = 'minus_cart'),

# remove cart in quantity 
    path('removecart/' , views.remove_cart , name = 'remove_cart'),    

    path('buy/', views.buy_now, name='buy-now'),


# profile and also address making url     
    path('profile/' , views.ProfileView.as_view() , name = "profile"),



    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name ='changepassword'),

# for mobile
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),


# for checkout 
path('checkout/', views.checkout, name='checkout'),
path('paymentdone/', views.payment_done, name='paymentdone'),

# for bottomwear
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/(?P<data>[-a-zA-Z0-9_]+)\\Z', views.bottomwear, name='bottomweardata'),


# for topwaer
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/(?P<data>[-a-zA-Z0-9_]+)\\Z', views.topwear, name='topweardata'),


# usig login form  django 
    path('accounts/login' , auth_views.LoginView.as_view(template_name = 'app/login.html' , 
    authentication_form = LoginForm) , name = "login"),


# usig logout form  django 
    path('logout/' , auth_views.LogoutView.as_view(next_page = "login") , name = "logout"),



# path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),


# password_reset on django
    path('password_reset/' , views.password_resert  , name = "password_reset") , 


# using change password django 
    path('passwordchange/' , auth_views.PasswordChangeView.as_view(template_name = 'app/passwordchange.html' ,
    form_class = MyPassowrdChangeForm , success_url = '/passwordchangedone/') , name = "passwordchange"),
    
    path('passwordchangedone/' , auth_views.PasswordChangeView.as_view (template_name = "app/passwordchangedone.html") , 
    name = "passwordchangedone"),

# forgate password
    path('password-reset/' , auth_views.PasswordResetView.as_view
    (template_name = 'app/password_reset.html' , form_class = MyPasswordResetForm) , name = "password_reset"),

    path('password-reset-done/' , auth_views.PasswordResetDoneView.as_view
    (template_name = 'app/password_reset_done.html') , name = "password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view
    (template_name = 'app/password_reset_confirm.html' , form_class = MySetPasswordForm) , name = "password_reset_confirm"),
     

    path('password-reset-complete/' , auth_views.PasswordResetCompleteView.as_view
    (template_name = 'app/password_reset_complete.html') , name = "password_reset_complete"),




] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
