
from django.shortcuts import render

# Create your views here.


def Blog_post(request):
    
    template_name = "blog.html"

    return render(request, template_name)