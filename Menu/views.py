from django.shortcuts import render,redirect
from django.http import HttpResponse
from Menu.models import Recipe
# Create your views here.
def mainpage(request):
    return render(request, "base.html")
def recipe(request):
    if request.method=="POST":
        data=request.POST # this can only be used to get the text data, for files such image, use request.FILES method as below
        veg_image=request.FILES.get("veg_image")
        print(data)
        for key in data:
            recipe_name=data["recipe_name"]
            #recipe_name=data.get("recipe_name"), Remember you are getting the json data, thats why the key is used
            veg_included=data.get("veg_included")
            recipe_descrip=data.get("recipe_descrip")             
        print(recipe_name)
        print(veg_included)
        print(recipe_descrip)
        print(veg_image)
        #the above is to print, but our pupose is to save the data for which we need to create the object as below (dont forget to import the models first)
        Recipe.objects.create(
          recipe_name=recipe_name,
          veg_included=veg_included,
          recipe_descrip=recipe_descrip,
          veg_image=veg_image
        )
        #without redirect everytime you reload a message will pop, after using it it will not show and directly reloads
        return redirect("/recipe/")
    #this is to visualize in frontend
    QuerySet=Recipe.objects.all()
    context={'recipes':QuerySet}
    #this context is parsed in recipe.html   
    return render(request, "htmlsss/recipe.html",context)

def delete_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipe/")
