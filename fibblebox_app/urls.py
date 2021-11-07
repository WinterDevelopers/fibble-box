from django.urls import path
from django.urls.resolvers import URLPattern

from .views import home, base, login, register, event, candidate, payment

app_name = 'fibblebox_app'

urlpatterns = [
    path('', home, name='home'),
    path('base' ,base, name='base'),
    path('login' ,login, name='login'),
    path('register', register, name='register'),
    path('<slug:slug>/', event, name='event'),
    path('candidate/<slug:id>/', candidate, name='candidate'),
    path('payment/<slug:id>/', payment, name='payment')

]