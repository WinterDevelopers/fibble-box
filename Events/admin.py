from django.contrib import admin
from .models import (Customer, Event, Sponsor, Ticket, Order, OrderItem, 
                    shippingDetails, Event_activities, Event_gallery,PurchasedTicket)

# Register your models here.
admin.site.register(Event)
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(shippingDetails)
admin.site.register(Event_activities)
admin.site.register(Event_gallery)
admin.site.register(Sponsor)
admin.site.register(PurchasedTicket)
