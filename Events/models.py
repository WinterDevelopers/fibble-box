from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

from Events import paystack


import secrets
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100,null=True)
    phrase = models.CharField(max_length=150,null=True)
    image = models.ImageField(upload_to='media/events', null=True)
    about = models.CharField(max_length=1000, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.CharField(max_length=100,null=True)
    video = models.FileField(upload_to='media/events/videos', null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    instagram = models.CharField(max_length=100,null=True)
    facebook = models.CharField(max_length=100, null=True)
    insight = models.PositiveIntegerField(default=0, null=True)

    @property
    def image_URL(self):
        try:
            image = self.image.url
        except:
            image = ''

        return image
    @property
    def video_URL(self):
        try:
            video = self.video.url
        except:
            video = ''
        
        return video

    @property
    def total_revenue(self):
        revenue = self.purchasedticket_set.all()
        total = sum([data.cost for data in revenue])
        return total

    def get_absolute_url(self):
        return reverse('Events:event', kwargs={'name':self.name})

    def __str__(self) -> str:
        return self.name

TICKET_CHIOCIES = (
    ('REGULER','regular'),
    ('VIP','vip'),
    ('BRONZE','bronze'),
    ('GOLD', 'gold'),
    ('PLATANIUM','platanium')
)

class Ticket(models.Model):
    name = models.CharField(max_length=70, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event')
    type = models.CharField(max_length=70,choices=TICKET_CHIOCIES, default='REGULAR')
    image = models.ImageField(upload_to='media/events/tickets',null=True)
    specification = models.CharField(max_length=1000, null=True)
    price = models.PositiveBigIntegerField(null=True)

    class Meta:
        ordering = ["type"]

    @property
    def image_URL(self):
        try:
            image = self.image.url
        except:
            image = ''

        return image

    def __str__ (self) -> str:
        return self.type


class Event_gallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/events/tickets', null=True)

    @property
    def image_URL(self):
        try:
            image = self.image.url
        except:
            image = ''

        return image

    def __str__(self) -> str:
        return str(self.event)

class Event_activities(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    header = models.CharField(max_length=70, null=True)
    content = models.CharField(max_length=500, null=True)

class Sponsor(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='media/events/sponsors', null=True)
    link = models.CharField(max_length=400, null=True)

    def image_URL(self):
        try:
            image = self.image.url
        except:
            image = ""
        return image

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=5000, null=True)
    date = models.DateField(auto_now_add=True)
   


    @property
    def total_quantity(self):
        orderitem = self.orderitem_set.all()
        total_quantity = sum([quantity.quantity for quantity in orderitem])

        return total_quantity

    @property
    def total_cost(self):
        orderitem = self.orderitem_set.all()
        total_cost = sum([total.total for total in orderitem])

        return total_cost

    @property
    def total_cost_paystack(self):
        total = self.total_cost * 100
        return total

    def save(self, *args, **kwargs):
        while not self.transaction_id:
            token = secrets.token_urlsafe(25)
            similar_token = Order.objects.filter(transaction_id=token)

            if not similar_token:
                self.transaction_id = token
            
            super().save(self)

    def completed_func(self, *args, **kwargs):
        self.completed = True
        super().save()

    def __str__(self):

        return str(self.id)


    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, default=0)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def total(self):
        total = self.ticket.price * self.quantity

        return total
    
  
    def __str__(self) -> str:
        return str(self.ticket)


from .paystack import Paystack

class shippingDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    verification_status = models.BooleanField(default=False)
    token = models.CharField( null=True, max_length=50)
    reference = models.CharField(max_length=400, null=True)

    def save(self, *args, **kwargs):
        while not self.reference:
            ref = secrets.token_urlsafe(20)
            similar_ref = shippingDetails.objects.filter(reference=ref)

            if not similar_ref:
                self.reference = ref
        super().save(*args, **kwargs)

    def verification(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.reference, self.amount)
      
        if status:
            if result['amount']/100 == self.amount:
                self.verification_status = True
                self.save()
            if self.verification_status:
                return True
            else:
                return False
            

    def __str__(self) -> str:
        return self.name


class PurchasedTicket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    code = models.CharField(null=True, max_length=20)
    type = models.CharField(null=True, max_length=30)
    cost = models.PositiveBigIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    date_purchased = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

