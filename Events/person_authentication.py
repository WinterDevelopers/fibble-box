from django import views
from django.http import HttpResponse
from django.shortcuts import redirect

def organizers(view_func):
    def wrapper_func(request,*args, **kwargs):
        group = request.user.groups.all()
        for a in group:
            if a:
                return view_func(request,*args, **kwargs)
               
        else:
            return redirect('home')
        
    return wrapper_func