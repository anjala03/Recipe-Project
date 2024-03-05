from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Recipe(models.Model):
    # user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    user=models.ForeignKey(User, on_delete=models.CASCADE )
    recipe_name=models.TextField()
    veg_included=models.CharField(max_length=100)
    recipe_descrip=models.TextField()
    veg_image=models.ImageField(upload_to="veges")
    def __str__(self)-> str:
        return self.recipe_name
#model/schema vege is created
    
