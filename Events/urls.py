from .views import (Event_index, Ticket_view, Shipping, Event_nav,ajax, shipping_process,cart_content_ajax,
                    reference, ticket_payment_verification, cart_arthemetics)
from django.urls import URLPattern, path


app_name = 'Events'

urlpatterns = [
    path('event_nav/', Event_nav, name='event_nav'),
    path('shipping/', Shipping, name='shipping'),
    path('ajax/', ajax, name='ajax'),
    path('cart-items',cart_content_ajax, name='cart-items' ),
    path('cart-arthemetics/', cart_arthemetics, name='cart-arthemetics'),
    path('reference/',reference,name='reference'),
    path('shipping_process',shipping_process, name='shipping_process'),
    path('<slug:name>/', Event_index, name='event'),
    path('ticket/<slug:name>/', Ticket_view, name='ticket'),
    path('payment-ticket-verification/<slug:token>', ticket_payment_verification, name='ticket_payment_verification')
    
]