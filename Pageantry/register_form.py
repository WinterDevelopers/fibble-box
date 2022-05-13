from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):

    first_name = forms.CharField(max_length=40, required=False, help_text='optional')
    last_name = forms.CharField(max_length=40, required=False, help_text='optional')
    email = forms.EmailField(max_length=50, help_text='this is required')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2')

       #''' widgets = {
            #'username':forms.TextInput(attrs={'class':'login-input'})
            #'first_name':forms.TextInput(attrs={'class':'login-name'})

        #}'''