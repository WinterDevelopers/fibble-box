from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    template_name = "register.html"
    context = {"form": form}
    return render(request, template_name, context)
