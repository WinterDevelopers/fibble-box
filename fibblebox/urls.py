"""fibblebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view


from Pageantry.views import home, logout_func, search_view
from Blog.sitemap import ViewSitemap

sitemaps = {
    'meta-data': ViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home' ),
    path('search', search_view, name='search'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    path('loggingout', logout_func, name='logout'),
    path('pageantry/', include('Pageantry.urls')),
    path('events/', include('Events.urls')),
    path('blog/', include('Blog.urls')),
    path('reset_password/', auth_view.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete',  auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete')

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

