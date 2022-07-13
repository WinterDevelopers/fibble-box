from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import (base, Login, register, pageantry, candidate, payment, payment_processor,
                    verify_payment, purchase_coupon, payment_coupon, coupon_delete, coupon_processor,
                    coupon_verify_payment, sending_coupon_codes,payment_delete, userPage, pagentries)

app_name = 'Pageantry'

urlpatterns = [
    path('',pagentries.as_view(), name='pageantry_page'),
    path('base' ,base, name='base'),
    path('login' ,Login, name='login'),
    path('register', register, name='register'),
    path('coupon-processing', coupon_processor, name='coupon_processor'),
    path('processing-payment', payment_processor, name='payment_processor'),
    path('delete-coupon', coupon_delete, name='delete_coupon'),
    path('purchase-coupons/',purchase_coupon, name= 'purchase_coupon'),
    path('user', userPage, name='user_page'),
    path('coupon-payment/<slug:token>/',payment_coupon, name ="coupon_payment"),
    path('<slug:slug>/', pageantry, name='pageantry'),
    path('candidate/<slug:id>/', candidate, name='candidate'),
    path('payment/<slug:id>/<slug:token>/', payment, name='payment'),
    path('payment-verification/<slug:reference>/', verify_payment, name='verify_payment'),
    path('payment-deleting',payment_delete, name='payment_delete'),
    path('coupon-verification/<slug:token>/',coupon_verify_payment, name= 'coupon_verification' ),
    path('sending_coupons/<slug:token>/',sending_coupon_codes, name='sending_coupons')
]