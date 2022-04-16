from django import forms
from django.forms import EmailInput, widgets
from django.forms import fields

from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('email',) 
    #email = forms.EmailField(widget = forms.EmailInput(attrs= {'class':'payment-email-field'}))

        