
from asyncio import events
from django.contrib.auth.models import User
from django.db import models

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

    @property
    def image_URL(self):
        try:
            image = self.image.url
        except:
            image = ''

        return image

    def video_URL(self):
        try:
            video = self.video.url
        except:
            video = ''
        
        return video

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=70, null=True)
    image = models.ImageField(upload_to='media/events/tickets',null=True)
    specification = models.CharField(max_length=1000, null=True)
    price = models.PositiveBigIntegerField(null=True)

    def __str__(self) -> str:
        return self.type+" for "+str(self.event)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


class OrderItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class shippingDetails(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)

class PurchasedTicket(models.Model):
    serial_number = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
