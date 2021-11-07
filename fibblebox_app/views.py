from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.

def home(request):
    events = Event.objects.all()
    
    template_name = 'index.html'
    context = {'events':events}

    return render(request, template_name, context)


def event(request, slug):
    template_name = 'event.html'

    event = get_object_or_404(Event, slug=slug)
    can = Candidate.objects.all()
    candidate = event.event_candidate.all()
    office  = event.event_office.all()
    percentage_votes = event.total_votes

    context = {'event':event, 'candidate':candidate, 'office':office, 'percentage_votes':percentage_votes, 'can':can}

    return render(request, template_name, context)


def candidate(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    coupon_code = votingCode.objects.all()
    coupon_list = []
    for x in coupon_code:
        coupon_list.append(x.coupon)

    print(coupon_list)

    if request.method == 'POST':
        code = request.POST.get('code')
        
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
            else:
                pass
            return redirect('fibblebox_app:candidate', candidate.id)
        else:
            print('code wrong')

    context = {'candidate':candidate}
    template_name = 'candidate.html'

    return render(request, template_name, context)



def base(request):

    template_name = 'base.html'

    return render(request, template_name)


def login(request):
    template_name = 'login.html'

    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)


    return render(request, template_name)


def register(request):
    template_name = 'register.html'

    return render(request, template_name)


from .payment_form import PaymentForm

def payment(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    template_name = 'initiate_payment.html'

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()
           
            return redirect('fibblebox_app:candidate', candidate.id)
        else:
            pass
    
    context = {"candidate":candidate}
    
    return render(request, template_name, context)


