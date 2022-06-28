from multiprocessing import context
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from Events.models import Customer, Event,Order, OrderItem, Ticket

from Pageantry.send_email import SendEmail
from .register_form import Registration

from .models import *

import json


def base(request):

    template_name = 'base.html'

    return render(request, template_name)


def Login(request):
    template_name = 'login.html'

    if request.method == 'POST':
       username = request.POST.get('username')
       print(username)
       password = request.POST.get('password')
       print(password)
       user = authenticate(username=username, password=password)
       if user:
        login(request, user)
        print('login!!!')
        return redirect('Events:event', 'LAMBA')
       else:
           print('failed!!!')
    return render(request, template_name)

def logout_func(request):

    logout(request)
    return redirect('home')

def register(request):
  
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username,password= raw_password)
            print(user)
            login(request, user)
            my_user = request.user
            customer = Customer.objects.create(user=my_user, name=name, email=email)
            my_cookie = json.loads(request.COOKIES['cart'])
            print(my_cookie)
            if my_cookie:
                order,created = Order.objects.get_or_create(customer=customer, completed = False)
                for i in my_cookie:
                    a = int(i)
                    ticket =  Ticket.objects.get(id=a)
                    OrderItem.objects.create(order=order, ticket=ticket, quantity=my_cookie[i]['quantity'])

            return redirect('Events:shipping')
        
    context = {'forms':form}
    template_name = 'register.html'
    return render(request, template_name, context)
# Create your views here.

def home(request):
    pageantries = Pageantry.objects.all()[:3]
    events  = Event.objects.all()[:3]
    
    template_name = 'index.html'
    context = {'pageantries':pageantries, 'events':events}

    return render(request, template_name, context)

def purchase_coupon(request):
    template_name = 'coupon_generator.html'

    if request.method == 'POST':
        number_of_coupons = request.POST.get('coupon_num_input')
        email = request.POST.get('email')
        token = request.POST.get('token')

        return redirect('Pageantry:coupon_payment', token)
        
    context = {'winter':'winter'}

    return render(request, template_name, context)

def payment_coupon(request, token):
    template_name = 'coupon_payment.html'

    public_key = settings.PUBLIC_KEY
    coupon_item = couponPayment.objects.get(token=token)
    coupon_email = coupon_item.email
    coupon_cost = coupon_item.amount
    coupon_votes = coupon_item.number_of_coupons
    context = {'email':coupon_email, "coupon":coupon_item, 'public_key':public_key, 'cost':coupon_cost, 'votes':coupon_votes}

    return render(request, template_name, context)


def pageantry(request, slug):
    template_name = 'pageantry.html'

    pageantry = get_object_or_404(Pageantry, slug=slug)
    candidate = pageantry.pageantry_candidate.all()
    office  = pageantry.pageantry_office.all()
    percentage_votes = pageantry.total_votes
    date = pageantry.date
    sponsors = pageantry.pageantry_sponsor.all()
   

    context = { 'pageantry':pageantry, 'candidate':candidate,
                'office':office, 'percentage_votes':percentage_votes, 
                'date':date, 'sponsors':sponsors}
   
    return render(request, template_name, context)


def candidate(request, id):
    
    candidate = get_object_or_404(Candidate, id=id)
    date = candidate.pageantry.date
    pageantry = candidate.pageantry
    sponsors = pageantry.pageantry_sponsor.all()
    coupon_code = votingCode.objects.all()
    share_string = 'vote me'
    coupon_list = []
    for x in coupon_code:
        coupon_list.append(x.coupon)
    #print(coupon_list)
    if request.method == 'POST':
        code = request.POST.get('code')
        input_vote = request.POST.get('candidate-vote-count')

        if code in coupon_list:
            print('code correct')
            coupon_code = votingCode.objects.get(coupon=code)
            ben = coupon_code
            print(ben.used_coupon)
            if coupon_code.used_coupon == False:
                coupon_code.used_coupon = True
                coupon_code.save()
                candidate.votes +=1
                candidate.save()
                messages.success(request,"vote was added")
            else:
                messages.error(request,"coupon invalid")
                
            return redirect('Pageantry:candidate', candidate.id)

        elif input_vote:
            payment_email = request.POST.get('email')
            token = request.POST.get('token')
            print(payment_email)
            input_vote_int = int(input_vote)

            if input_vote_int > 0:
                vote_amount = input_vote_int * 100
            
                return redirect('Pageantry:payment', candidate.id, token )

            return redirect('Pageantry:candidate', candidate.id)

        else:
            print('code wrong')

    context = {'candidate':candidate, 'share_string':share_string, 'date':date, 'sponsors':sponsors}
    template_name = 'candidate.html'

    return render(request, template_name, context)

from .payment_form import PaymentForm

import json


def payment(request, id, token):
    template_name = 'initiate_payment.html'
    public_key = settings.PUBLIC_KEY
    candidate = Candidate.objects.get(id=id)
    payment = Payment.objects.get(candidate=candidate, verification_status=False, token=token)

    if request.method == 'POST':
        
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            
            payment_form.save()                                            
    else:
        payment_form = PaymentForm()

    context = {'payment_form':payment_form, 'candidate':candidate, 'payment':payment, 'public_key':public_key}
    
    return render(request, template_name, context)


def verify_payment(request:HttpRequest, reference):
    payment = get_object_or_404(Payment, reference=reference)
    candidate = get_object_or_404(Candidate, name= payment.candidate)
    print(candidate)
    
    verified = payment.verified_payment()
    messages.error(request, "verified")

    return redirect('Pageantry:candidate', candidate.id )
    amount = payment.amount
    #print(verified)
    if verified:
        votes = amount/100
        candidate.votes += votes 
        candidate.save()
        messages.success(request, f"verification successful, your {votes} vote(s) was added")
    else:
        messages.error(request, "verification failed!!")

    return redirect('Pageantry:candidate', candidate.id )

def coupon_verify_payment(request:HttpRequest, token):
    coupon_payment = get_object_or_404(couponPayment, token=token)
    verified = coupon_payment.verified_payment()

    if verified:
        messages.success(request, 'coupon purchasing was successful')

    else:
        messages.error(request, 'coupon_purchasing failed')

    return redirect('Pageantry:sending_coupons', coupon_payment.token )


from .coupon_generator import CouponGenerator

def sending_coupon_codes(request, token):

    customer = get_object_or_404(couponPayment, token=token)
    customer_email = customer.email
    numbers_coupons = customer.number_of_coupons
    the_coupons = CouponGenerator()
    coupon_codes = the_coupons.generator(numbers_coupons)
    print (coupon_codes)

    for x in coupon_codes:
        code = x
        voting_coupons = votingCode.objects.create(coupon=code)
        voting_coupons.save()
        
    with open('voting_coupons.txt', 'w') as file:
        for a in coupon_codes:
            file.write('%s \n'% a)

    send_email = SendEmail()
    sending_email = send_email.sending_email(customer_email)
    if sending_email:
        return redirect('home')
    return redirect('Pageantry:login')

@login_required(login_url='Pageantry:login')
def userPage(request):
    template_name = 'user_page.html'

    context = {}

    return render(request, template_name, context)

# MY FETCH VIEW FUNCTIONS////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////

def payment_processor(request):
    print('look')
    data = json.loads(request.body)
    email = data['email']
    number_votes = data['votes']
    candidate_id = int(data['candidate_id'])
    token = data['token']
    amount = 100*int(number_votes)
    amount_int = int(amount)
    print(number_votes,'can id: ',amount)

    candidate = Candidate.objects.get(id=candidate_id)
    the_customer= Payment.objects.create(candidate=candidate)
    print('candidate :',the_customer)
    the_customer.amount = amount_int
    the_customer.email = email
    the_customer.token = token
    the_customer.save()
    print("i saved the amount")
    
    return JsonResponse('i worked', safe=False)

def coupon_processor(request):
    print('was called')
    data = json.loads(request.body)
    email = data['email']
    number_of_coupons = data['number_of_coupons']
    token = data['token']
    amount = int(number_of_coupons)*100
   
    if not int(number_of_coupons ) <= 0:
        coupon_payment = couponPayment.objects.create(number_of_coupons=number_of_coupons)
        coupon_payment.email = email
        coupon_payment.token = token
        coupon_payment.amount = amount
        coupon_payment.save()
    else:
        pass

    return JsonResponse('sent the coupon data', safe=False)

def coupon_delete(request):
    data = json.loads(request.body)
    token = data['token']
    coupon = get_object_or_404(couponPayment, token=token)
    coupon.delete()
    print(token)
    return JsonResponse('deleted the coupon', safe=False)

def payment_delete(request):
    data = json.loads(request.body)
    ref = data['ref']
    print(ref)
    payment = get_object_or_404(Payment, reference=ref)
    if not payment.verification_status:
        payment.delete()
    else:
        pass

    return JsonResponse('deleted successfully', safe=False)
