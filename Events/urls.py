from .views import (Event_index, Ticket_view, Shipping, Event_nav,ajax, events_page, shipping_process,cart_content_ajax,
                    reference, ticket_payment_verification, cart_arthemetics, checking_in, check_ticket, dashboard)
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_view


app_name = 'Events'

urlpatterns = [
    path('', events_page.as_view(), name='events_page'),
    path('event_nav/', Event_nav, name='event_nav'),
    path('shipping/', Shipping, name='shipping'),
    path('ajax/', ajax, name='ajax'),
    path('checking_in', checking_in, name='delete_shipping'),
    path('cart-items',cart_content_ajax, name='cart-items' ),
    path('cart-arthemetics/', cart_arthemetics, name='cart-arthemetics'),
    path('reference/',reference,name='reference'),
    path('shipping_process/',shipping_process, name='shipping_process'),
    path('dashboard/<slug:name>', dashboard, name='dashboard'),
    path('check-ticket/<slug:ticket_id>/', check_ticket, name='check_ticket'),
    path('<slug:name>/', Event_index, name='event'),
    path('ticket/<slug:name>/', Ticket_view, name='ticket'),
    path('payment-ticket-verification/<slug:token>', ticket_payment_verification, name='ticket_payment_verification')
    
    

]