from distutils.command.upload import upload
import email
from email.mime import image
from lib2to3.pgen2 import token
from pyexpat import model
from attr import attr
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.forms import forms, widgets
from django.urls import reverse
from django.contrib import messages

from .paystack import Paystack


import secrets


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    username  = models.CharField(max_length=150)
    password = models.CharField( max_length=200) 

    def __str__(self):
        return self.username



CATEGORIES = [
    ('pg','pagentry'),
    ('aw','awards'),
    ('su','survey'),
    ('cm' ,'comperism')

]

class Pageantry(models.Model):
    name = models.CharField(max_length=250,default="default text")
    slug = models.SlugField(max_length=250, unique=True)
    pageantry_image = models.ImageField(upload_to = 'media/pageantry')
    pageantry_banner = models.ImageField(upload_to = 'media/pageantry')
    pageantry_info = models.CharField(max_length=3000, null=True)
    category = models.CharField(choices=CATEGORIES, max_length=2, null=True)
    intro_text = models.CharField(max_length=250, default="default text")
    discription = models.CharField(max_length=450, null=True)
    date = models.DateField()
    count_down = models.DateTimeField()

    @property
    def total_votes(self):
        candidate_vote = self.pageantry_candidate.all()
        pageantry_votes = sum([vote.votes for vote in candidate_vote])

        return pageantry_votes

    @property
    def pageantryImage(self):
        try:    
            url = self.pageantry_image.url
        except:
            url = ''
        return url

    @property
    def pageantryBanner(self):
        try:
            url = self.pageantry_banner.url
        except:
            url = ''
        return url

    def get_absolute_url(self):

        return reverse('Pageantry:pageantry', kwargs={'slug':str(self.slug)})

    def __str__(self):
        return self.name


class Office(models.Model):
    pageantry = models.ForeignKey(Pageantry, on_delete=models.CASCADE, related_name='pageantry_office')
    office_name = models.CharField(max_length=200)

    @property
    def office_total_votes(self):
        votes = self.candidate_office.all()
        
        office_votes = sum([x.votes for x in votes])
        
        return office_votes


    def __str__(self):
        return self.office_name

class Candidate(models.Model):
    pageantry = models.ForeignKey(Pageantry, on_delete=models.CASCADE, related_name='pageantry_candidate', null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='candidate_office', null=True)
    name = models.CharField(max_length=100)
    quote = models.CharField(max_length=250)
    background_image = models.ImageField(upload_to = 'media/candidates')
    personal_image = models.ImageField(upload_to = 'media/candidates')
    votes = models.IntegerField()

    @property
    def background_image_URL(self):
        try:
            image = self.background_image.url
        except:
            image = ''
        return image

    @property
    def personal_image_URL(self):
        try:
            image = self.personal_image.url
        except:
            image = ''
        return image
    
    #@property
    #def percentage_votes(self):
        total_votes = sum([vote  for vote in range(0,self.votes - 1)])
        return total_votes

    @property
    def office_name(self):
        return str(self.office)


    def get_absolute_url(self):

        return reverse('Pageantry:candidate', kwargs={'id':str(self.id)})


    def __str__(self):
        return self.name



class votingCode(models.Model):
    #pageantry = models.ForeignKey(Pageantry, on_delete=models.CASCADE, related_name='pageantry_code', null=True)
    coupon = models.CharField(max_length=30)
    used_coupon = models.BooleanField(default=False)
    time_used = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.coupon)

class couponPayment(models.Model):
    number_of_coupons = models.PositiveIntegerField(null=True)
    email = models.EmailField(null=True)
    amount = models.PositiveIntegerField(null=True)
    token = models.CharField(max_length=200,null=True)
    verification = models.BooleanField(default=False)
    reference = models.CharField(max_length=100, null=True)

    class Meta:
        ordering =['-token']

    def save(self, *args, **kwargs)->None:
        while not self.reference:
            reference = secrets.token_urlsafe(40)
            similiar_ref = couponPayment.objects.filter(reference=reference)
            if not similiar_ref :
                self.reference = reference
        super().save(*args, **kwargs)

    def amount_value(self) ->int:
        amount = self.amount * 100
        return amount

    def verified_payment(self) -> bool:
        paystack = Paystack()
        status, result = paystack.verify_payment(self.reference, self.amount_value)
        
        if status:
            if result['amount']/100 == self.amount:
                self.verification = True
            self.save()
        if self.verification:
            return True
        else:
            return False

    def __str__(self):
        return str(self.amount)





class Payment(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(null=True)
    email = models.EmailField(null=True)
    reference = models.CharField(max_length=100, null=True)
    verification_status  = models.BooleanField(default=False)
    date_of_transaction = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=300, null=True)

    class Meta:
        ordering =['-date_of_transaction']

    def save(self, *args, **kwargs) ->None:
        while not self.reference:
            reference = secrets.token_urlsafe(30)
            similar_reference  = Payment.objects.filter(reference=reference)
            if not similar_reference:
                self.reference = reference

        super().save(*args, **kwargs)

    def amount_value(self) ->int:
        amount = self.amount * 100
        return amount

    def verified_payment(self) -> bool:
        paystack = Paystack()
        status, result = paystack.verify_payment(self.reference, self.amount_value)
        
        if status:
            if result['amount']/100 == self.amount:
                self.verification_status = True
            self.save()
        if self.verification_status:
            return True
        else:
            return False


    def __str__(self) -> str:
        return f"payment of:{self.amount} for {self.candidate}"


class pageantrySponsor(models.Model):
    pageantry = models.ForeignKey(Pageantry, on_delete=models.CASCADE, null=True, related_name="pageantry_sponsor")
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/sponsors')

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image

    def __str__(self) -> str:
        return self.name