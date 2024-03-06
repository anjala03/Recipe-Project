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

# app_name = "Menu"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('basepage/', basepage, name="basepage"),
    path('add_recipe/', add_recipe, name="add_recipe"),
    path('delete/<int:id>/', delete_recipe, name="delete_recipe"),
    path('search/', search_recipe, name="search"),
    path('show_recipes/', show_recipes, name="show_recipes"),
    path('update/<int:id>/', update, name="update"),
    path('success_msg/', success_msg, name="success_msg"),
    path('login/', loginpage, name="loginpage"),
    path('register/', register, name="register"),


  



]
# this (the below if sectio) has to be done for every media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)