from django.shortcuts import render,redirect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from Menu.models import Recipe
# Create your views here.
def basepage(request):
    return render(request, "base.html")

def add_recipe(request):
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
        return redirect("/success_msg/")

        return render(request, "htmlsss/add_recipe.html", context= {"recipe_name":recipe_name, "veg_included":veg_included,"recipe_descrip":recipe_descrip, "veg_image" :veg_image})
        #without redirect everytime you reload a message will pop, after using it it will not show and directly reloads
       
    

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
    recipe = get_object_or_404(Recipe, id=id)
    # this is to check if the id is available or not, it wil return none in case no such id is available. Has to pass the modle name as the first parameter
    recipe.delete()
    return redirect("/show_recipes")


#def delete_recipe(request, id):
#    print(id)
#    queryset=Recipe.objects.get(id = id)
#    queryset.delete()
#    return redirect("/show_recipes")

def search_recipe(request):
    if request.method=="POST":
        recipe_Name=request.POST.get("query").strip()
        # the Q string is used to encapsulate the filter even more. The starts with check the starting word and search if the searced keyword matches or not.
        # the icontains is used to handle case sensitivity.
        desired_recipe=Recipe.objects.filter(Q(recipe_name__startswith=recipe_Name)|Q(recipe_name__icontains=recipe_Name))
        context={"desired_recipe":desired_recipe}
        return render(request, "htmlsss/search_recipe.html", context)
    return render(request, "recipe.html")
    
def success_msg(request):
    return render (request, "htmlsss/success.html")
    
def login(request):
    return render(request, "htmlsss/login.html")


def register(request):
    if request.method== "POST":
        data=request.POST
        firstname= data.get("firstname")
        lastname= data.get("lastname")
        username= data.get("username")
        password=data.get("password")
        User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname
            )
        return render (request, "htmlsss/register.html", context= {"success_msg":"Registration done successfully"})
    return render(request, "htmlsss/register.html", context={"firstname":[], "lastname":[], "username":[], "password":[]})



    
