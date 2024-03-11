from django.contrib import admin
from .models import * #import the models first
# Register your models here.
admin.site.register(Recipe)
#for registring admin.site.register this is same for all in the braces you have to pass the models classname which you want to display,  you can pass many models here
admin.site.register(Department)
admin.site.register(Student_id)
admin.site.register(Student)


