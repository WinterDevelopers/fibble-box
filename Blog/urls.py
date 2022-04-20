from django.urls import path

from .views import Blog_post

app_name = "Blog"

urlpatterns = [

    path('talk', Blog_post, name='talk'),
]