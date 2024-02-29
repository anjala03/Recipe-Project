"""recipesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from Menu.views import *
from django.conf import settings
#settings and static must be imported for media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', mainpage, name="mainpage"),
    path('recipe/', recipe, name="recipe"),
    path('delete/<id>/', delete_recipe, name="delete_recipe"),

]
# this (the below if sectio) has to be done for every media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)