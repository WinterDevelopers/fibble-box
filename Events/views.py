
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def Event(request):

    template_name = 'events.html'

    return render(request, template_name)

def Ticket(request):

    template_name = 'ticket.html'

    return render(request, template_name)

def Cart(request):

    template_name = 'cart.html'

    return render(request, template_name)

def Shipping(request):

    template_name = 'shipping.html'

    return render(request, template_name)
