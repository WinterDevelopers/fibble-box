from re import template
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def Event(request):

    template_name = 'events.html'

    return render(request, template_name)