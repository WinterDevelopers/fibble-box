from django.urls import path

from .views import home, post_detail, add_post, edit_post, delete_post, become_writer


app_name = "Blog"

urlpatterns = [
    path('', home, name='talk'),
    path('add-post/', add_post, name='add-post'),
    path('<slug:slug>/er/', post_detail, name='post-detail'),
    path('<slug:slug>/edit/', edit_post, name='edit-post'),
    path('<slug:slug>/delete/', delete_post, name='delete-post'), 
    path('join/become-writer/', become_writer, name="become-writer")  
]