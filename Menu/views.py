from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainpage(request):
    return render(request, "base.html")
def recipe(request):
    if request.method=="POST":
        data=request.POST
        for each_data in data:
            recipe_name=each_data.get("recipe_name")
            print(recipe_name)
            veg_included=each_data.get("veg_included")
            print(veg_included)
            recipe_descrip=each_data.get("recipe_descrip")
            print(recipe_descrip)
            veg_image=each_data.get("veg_image")
        
    
    
    return render(request, "htmlsss/recipe.html")