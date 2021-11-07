from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.urls import reverse



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

class Event(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    event_image = models.ImageField(upload_to = 'media/events')
    event_banner = models.ImageField(upload_to = 'media/events')
    category = models.CharField(choices=CATEGORIES, max_length=2)
    intro_text = models.CharField(max_length=250)
    discription = models.CharField(max_length=450)
    date = models.DateField()
    count_down = models.DateTimeField()

    @property
    def total_votes(self):
        candidate_vote = self.event_candidate.all()
        event_votes = sum([vote.votes for vote in candidate_vote])

        return event_votes

    @property
    def eventImage(self):
        try:
            url = self.event_image.url
        except:
            url = ''
        return url

    @property
    def eventBanner(self):
        try:
            url = self.event_banner.url
        except:
            url = ''
        return url

    def get_absolute_url(self):

        return reverse('fibblebox_app:event', kwargs={'slug':str(self.slug)})

    def __str__(self):
        return self.name


class Office(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_office')
    office_name = models.CharField(max_length=200)

    def __str__(self):
        return self.office_name

class Candidate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_candidate')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='candidate_office', null=True)
    name = models.CharField(max_length=100)
    quote = models.CharField(max_length=250)
    background_image = models.ImageField()
    personal_image = models.ImageField()
    votes = models.IntegerField()

    @property
    def background_image_URL(self):
        try:
            image =   self.background_image.url
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

        return reverse('fibblebox_app:candidate', kwargs={'id':str(self.id)})


    def __str__(self):
        return self.name



class votingCode(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_code')
    coupon = models.CharField(max_length=30)
    used_coupon = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event)


class Payment(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    email = models.EmailField()
    reference = models.CharField(max_length=100)


    def __str__(self) -> str:
        return str(self.candidate)