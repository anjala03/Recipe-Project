from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True ,default=None)
    # user=models.ForeignKey(User, on_delete=models.CASCADE )
    recipe_name=models.TextField()
    veg_included=models.CharField(max_length=100)
    #have to mention max_length when using charfield
    recipe_descrip=models.TextField()
    veg_image=models.ImageField(upload_to="veges")
    def __str__(self)-> str:
        return self.recipe_name
    recipe_view_count=models.IntegerField(default=1)
    #default is set to one
#model/schema Recipe is created
    
class Department(models.Model):
    department=models.TextField()
    def __str__(self)->str:
        return self.department
    
    class Meta:
        ordering=["department"]

class Student_id(models.Model):
    student_id=models.CharField(max_length=50)
    def __str__(self)->str:
        return self.student_id
    class Meta:
        ordering=["student_id"]

class Student(models.Model):
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id=models.OneToOneField(Student_id, on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()
    student_email=models.EmailField(default=None)
    def __str__(self)->str:
        return self.student_name


    
