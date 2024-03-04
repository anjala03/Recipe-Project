from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
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
        
        recipe_name=data["recipe_name"]
        #recipe_name=data.get("recipe_name"), Remember you are getting the json data, thats why the key is used
        veg_included=data.get("veg_included")
        recipe_descrip=data.get("recipe_descrip")             
        
        #the above is to print, but our pupose is to save the data for which we need to create the object as below (dont forget to import the models first)
        Recipe.objects.create(
          recipe_name=recipe_name,
          veg_included=veg_included,
          recipe_descrip=recipe_descrip,
          veg_image=veg_image
        )
        # return redirect("/recipe/")

        return render(request, "htmlsss/add_recipe.html", context= {"recipe_name": recipe_name, "veg_included": veg_included, "recipe_descrip":recipe_descrip,"veg_image": veg_image})
        #without redirect everytime you reload a message will pop, after using it it will not show and directly reloads
        # return redirect("/recipe/")
    #this is to visualize in frontend
    elif(request.method=="GET"):
        return render(request, "htmlsss/add_recipe.html", context= {"recipe_name": [], "veg_included": [], "recipe_descrip":[],"veg_image": []})
#this is done because as  whenever you use post method there is by default the usecase of get method  which will show the template only, so the empty list is parsed there



def show_recipes(request):
    QuerySet=Recipe.objects.all()
    context={'recipes':QuerySet}
    #this context is parsed in recipe.html   
    return render(request, "htmlsss/show_recipe.html",context)

def delete_recipe(request, id):
    print(id)
    queryset=Recipe.objects.get(id = id)
    queryset.delete()
    return redirect("/recipe/")

def search_recipe(request):
    if request.method=="POST":
        recipe_Name=request.POST.get("query")
        desired_recipe=Recipe.objects.filter(recipe_name=recipe_Name)
        context={"desired_recipe":desired_recipe}
        return render(request, "htmlsss/search_recipe.html", context)
    return render(request, "recipe.html")
    
    


    
