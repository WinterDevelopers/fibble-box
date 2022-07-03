from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

  
    class Meta:
        model = User
        fields = "__all__"

       #''' widgets = {
            #'username':forms.TextInput(attrs={'class':'login-input'})
            #'first_name':forms.TextInput(attrs={'class':'login-name'})

        #}'''