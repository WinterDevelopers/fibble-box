from django.urls import path

from .views import posts_list, post_detail, add_post, edit_post, delete_post, become_writer


app_name = "Blog"

urlpatterns = [
    path('', posts_list, name='talk'),
    path('posts/add/', add_post, name='add-post'),
    path('posts/<slug:slug>/', post_detail, name='post-detail'),
    path('posts/<slug:slug>/edit/', edit_post, name='edit-post'),
    path('posts/<slug:slug>/delete/', delete_post, name='delete-post'), 
    path('join/become-writer/', become_writer, name="become-writer")  
]