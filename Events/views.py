from django.conf import settings

import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from numpy import True_

from .models import Event, Event_activities, Event_gallery, Order, OrderItem, Sponsor,Ticket, shippingDetails, PurchasedTicket

from .ticket_processor import Ticket_processing

from django.views.generic.list import ListView
# Create your views here.

class events_page(ListView):
    template_name: str = 'event_page.html'
    model = Event
    paginate_by: int = 5

    def get_context_data(self,*args, **kwargs):

        context = super(events_page, self).get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-id')[:1]

        return context



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

    event.insight = (event.insight +1)
    #print(event.insight)
    event.save()

    if request.user.is_authenticated:
        item = 0
    else:
        item = 1
    

    context = {'event':event, "event_gallery":event_gallery,'item':item,
                'event_activities':event_activities, "sponsors":sponsors}
    
    return render(request, template_name, context)

def Ticket_view(request, name):
    
    event = get_object_or_404(Event, name=name)
    tickets = Ticket.objects.filter(event=event)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, completed=False)
        item = order.orderitem_set.all()
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
            print('cart',cart)
        item = []
        order = {'quantity':0,'total_quantity':0,'total_cost':0}
        cartItem = order['quantity']

        for i in cart:
            cartItem += cart[i]['quantity']
            ticket = Ticket.objects.get(id=i)

            total = (ticket.price * cart[i]['quantity'])
            order['total_cost'] += total
            order['total_quantity'] += cart[i]['quantity']




    context = {"event":event,"tickets":tickets, 'item':item, 'order':order}
    template_name = 'ticket.html'

    return render(request, template_name, context)

@login_required(login_url='Pageantry:login')
def Shipping(request):
    my_user = request.user
    print(my_user)
    customer = request.user.customer
    order = get_object_or_404(Order, customer=customer, completed=False)
    public_key = settings.PAYSTACK_PUBLIC_KEY
    event = {'name':'LAMBA'}
    context = {'order':order, 'public_key':public_key, 'event':event}
    template_name = 'shipping.html'

    return render(request, template_name, context)




def check_ticket(request, ticket_id):
   
    ticket = PurchasedTicket.objects.get(code=ticket_id)
    name = ticket.name
    type = ticket.type
    event = ticket.event
    groups = 'none'
    if not str(request.user )== 'AnonymousUser':
        groups = request.user.groups.all()

    group_list = []
    auth = False
    for group in groups:
       group_str = str(group)
       event_str = str(event)
       group_list.append(group_str)
       
    if  event_str in group_list:
        auth = True
    
    if not ticket.status:
        status = "VALID"
    else:
        status = "USED"
    context = {'ticket_id':ticket_id, 'name':name,'auth':auth,
    'type':type, 'status':status, 'event':event}
    template_name = 'ticket_checker.html'

    return render(request,template_name, context)
from Events.person_authentication import organizers


@organizers
def dashboard(request,name):
    groups = request.user.groups.all()
    for group in groups:
        group_str = str(group)
    if not name in group_str:
        return redirect('home')
    count = PurchasedTicket.objects.count()    
    event = Event.objects.get(name=name)
    template_name = "event_dashboard.html"
    ticket = PurchasedTicket.objects.all()
    def totalRevenue():
        if event.total_revenue >= 1000000:
            value_int = "%.1f %s"%(event.total_revenue/1000000,'M')
        elif event.total_revenue >= 1000:
            value_int = "%.1f %s"%(event.total_revenue/1000,'K')
        else:
            value_int = event.total_revenue
        return value_int
    def views():
        if event.insight >= 1000000:
            views = "%.1f %s"%(event.insight/1000000, 'M')
        elif event.insight >= 1000:
            views = "%.1f %s"%(event.insight/1000, 'k')
        else:
            views = event.insight
        return views
    view = views
    revenue = totalRevenue

    context = {'event':event, 'count':count, 'views':view, 'revenue':revenue, 'tickets':ticket}

    return render(request, template_name, context)
    
#//////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////

def ticket_payment_verification(request, token):
    customer = request.user.customer
    payment = get_object_or_404(shippingDetails, token=token, verification_status=False)
    order = get_object_or_404(Order, customer=customer, completed=False)
  
    verified = payment.verification()
    if verified:
        ticket_processing = Ticket_processing()
        ticket_processing.ticket_image(customer)
        #print(order.completed)
        order.completed_func()
        messages.success(request, 'your ticket was sucessfully purchased and sent to your E-mail')
        
        return redirect('Events:event', "LAMBA")

    else:
        messages.error(request, 'ticket purchasing failed due to unverified transaction')
    return redirect('Events:shipping')


#//////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////

def ajax(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = get_object_or_404(Order,customer=customer, completed=False)
        quan = order.total_quantity
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        order = {'total_quantity':0}

        for i in cart:
            order['total_quantity'] += cart[i]['quantity']
        quan= order['total_quantity']
    
    return JsonResponse({'number':quan, }, status=200)

def cart_content_ajax(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = get_object_or_404(Order,customer=customer, completed=False)
        orderitem = get_object_or_404(OrderItem, order=order)
        items = {}
        for a in orderitem:
            content = {'quantity':a.quantity,'price':a.price}
            items[a.name]=content



    else:
        try:
            cookies = json.loads(request.COOKIES['cart'])
        except:
            cookies = {}
        items={'hey':2}
    return JsonResponse({'orderitem':items}, status=200)
        

def cart_arthemetics(request):
    customer = request.user.customer
    event = get_object_or_404(Event, name='LAMBA')
    ticket = get_object_or_404(Ticket, id=request.POST.get('id'))
    order = get_object_or_404(Order,customer=customer, completed=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, ticket=ticket)
    action = request.POST.get('action')
    print(action)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
        orderitem.save()
        print('addded')

    elif action == 'minus':
        if orderitem.quantity > 1:
            orderitem.quantity = (orderitem.quantity - 1)
            orderitem.save()
            print('removed')
        else:
            orderitem.delete()
            print('deleted')

    return JsonResponse('worked', safe=False, status=200)

def shipping_process(request):
    customer = request.user.customer
    order = get_object_or_404(Order, customer=customer, completed=False)
    try:
        shipping_exists = shippingDetails.objects.get(order=order)
    except:
        shipping_exists = False
    print('see it',shipping_exists)
    if shipping_exists:
        shipping_exists.delete()
    data = json.loads(request.body)
    name = data['name']
    email = data['email']
    phone = data['phone']
    amount = data['order_amount']
    token = data['token']
    #print(data)

    shippingDetails.objects.create(name=name, email=email,order=order, amount=amount, token=token)

    return JsonResponse('shipping details gotten and created', safe=False)

def reference(request):

    customer = request.user.customer
    order = get_object_or_404(Order, customer=customer, completed=False)
    shipping = get_object_or_404(shippingDetails,order=order,verification_status=False )

    reference = shipping.reference
    token = shipping.token

    return JsonResponse({'reference':reference, 'token':token} ,safe=False, status = 200)

def checking_in(request):

    data = json.loads(request.body)
    transact_id = data['id']
    purchase_ticket = get_object_or_404(PurchasedTicket, code=transact_id)
    purchase_ticket.status = True
    purchase_ticket.save()
    return JsonResponse('checked_in', safe=False)
