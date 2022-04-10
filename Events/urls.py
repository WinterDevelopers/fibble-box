from .views import Event
from django.urls import URLPattern, path


app_name = 'Events'

urlpatterns = [
    path('winter', Event, name='event'),
]