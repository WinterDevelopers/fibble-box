from .views import Event, Ticket, Cart, Shipping
from django.urls import URLPattern, path


app_name = 'Events'

urlpatterns = [
    path('winter', Event, name='event'),
    path('ticket', Ticket, name='ticket'),
    path('cart', Cart, name='cart'),
    path('shipping', Shipping, name='shipping'),
]