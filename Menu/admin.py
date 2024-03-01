from django.contrib import admin
from .models import Recipe #import the models first
# Register your models here.
admin.site.register(Recipe)
#for registring admin.site.register this is same for all in the braces you have to pass the models classname which you want to display,  you can pass many models here