
from asyncio import events
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Event_activities, Event_gallery, Sponsor

# Create your views here.
def Event_nav(request):
    template_name = 'event_base.html'
    context = {}

    return render(request, template_name, context)


def Event_index(request, name):
    template_name = 'events.html'

    event = get_object_or_404(Event, name=name)
    event_gallery = Event_gallery.objects.filter(event=event)
    event_activities = Event_activities.objects.filter(event=event)
    sponsors = Sponsor.objects.filter(event=event)
    

    context = {'event':event, "event_gallery":event_gallery,'item':3,
                'event_activities':event_activities, "sponsors":sponsors}
    
    return render(request, template_name, context)

def Ticket(request):

    template_name = 'ticket.html'

    return render(request, template_name)

def Shipping(request):

    template_name = 'shipping.html'

    return render(request, template_name)
