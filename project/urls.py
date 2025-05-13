"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls.static import static
from rest_framework import permissions

from project import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.urls')),
    path('units/', include('apps.units.urls')),
    path('news/', include('apps.news.urls')),
    path('studentportal/', include('apps.studentportal.urls')),
    path('services/', include('apps.services.urls')),
    path('users/', include('apps.users.urls')),
   path('academics/', include('apps.academics.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
