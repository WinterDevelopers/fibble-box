from .views import Event_index, Ticket, Shipping, Event_nav
from django.urls import URLPattern, path


app_name = 'Events'

urlpatterns = [
    path('event_nav/', Event_nav, name='event_nav'),
    path('ticket', Ticket, name='ticket'),
    path('shipping', Shipping, name='shipping'),
    path('<slug:name>/', Event_index, name='event'),
]