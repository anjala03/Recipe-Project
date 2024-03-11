from django.shortcuts import render,redirect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from Menu.models import Recipe
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
# Create your views here.
def basepage(request):
    return render(request, "base.html")

#login required is the decorators which will ensure that the add recipe page will only be acessed after login is successfull

@login_required(login_url='/login/')
# in case to redirect the user to the login page when tried to access without loging in (if this not done only the error message is displayed), have to define LOGIN_URL in settings.py as LOGIN_URL = '/login/' OR you can pass it as a parameter in the function as login_url='/login/'
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


@login_required(login_url='/login/') 
def show_recipes(request):
    QuerySet=Recipe.objects.all()
    context={'recipes':QuerySet}
    #this context is parsed in recipe.html   
    return render(request, "htmlsss/show_recipe.html",context)


@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def update(request, id):
    recipe_obj= get_object_or_404(Recipe, id=id)
    if request.method=="POST":
        data=request.POST
        Recipe_Name=data.get("recipe_name")
        Veg_Included=data.get("veg_included")
        Recipe_Descrip=data.get("recipe_descrip")

        if Recipe_Name:
          recipe_obj.recipe_name=Recipe_Name
        if Veg_Included:
          recipe_obj.veg_included=Veg_Included
        if Recipe_Descrip:
          recipe_obj.recipe_descrip=Recipe_Descrip
        
        recipe_obj.save()

        return redirect("/show_recipes")
    
    elif (request.method=="GET"):
        recipe_obj= get_object_or_404(Recipe, id=id)
        return render(request, "htmlsss/update.html", context={"recipe_obj":recipe_obj})

@login_required(login_url='/login/')
def search_recipe(request):
    if request.method=="POST":
        recipe_Name=request.POST.get("query").strip()
        # the Q string is used to encapsulate the filter even more. The starts with check the starting word and search if the searced keyword matches or not.
        # the icontains is used to handle case sensitivity.
        desired_recipe=Recipe.objects.filter(Q(recipe_name__startswith=recipe_Name)|Q(recipe_name__icontains=recipe_Name))
        context={"desired_recipe":desired_recipe}
        return render(request, "htmlsss/search_recipe.html", context)
    return render(request, "htmlsss/add_recipe.html")
    
def success_msg(request):
    return render (request, "htmlsss/success.html")
    
def loginpage(request):
    if request.method== "POST":
        data=request.POST
        username= data.get("username")
        password=data.get("password")
        if User.objects.filter(username=username).exists():
            #autheticate method is used to check the credentails mapping with the database, if the credentials are right returns the user object else returns the None
            user=authenticate(username=username, password=password)
            if user is not None:
                #this is to maintain the session the use of login method which uses two parameters request and userobject
                login(request, user)
                return redirect ("/add_recipe")
            messages.error(request, "Invalid Credentials")
            return redirect("/login")
        messages.error(request, "Invalid Username") 
        return redirect("/login")
    return render(request, "htmlsss/login.html", context={"username":[], "password":[]})
      


def register(request):
    if request.method== "POST":
        data=request.POST
        firstname= data.get("firstname")
        lastname= data.get("lastname")
        username= data.get("username")
        password=data.get("password")
        
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect ("/register")
        user=User.objects.create(
            username=username,
            first_name=firstname,
            last_name=lastname
            #in django database the first_name, last_name is by default , in case of use of any thing other than this may throw some errors

            )
        #this is done so that password is hashed, the set password method changes password into something that is not understandable.
        user.set_password(password)
        user.save()
        messages.info(request, "Congratulations!!!Registration done successfully.")
        #messages takes two parameters, request and the mesage you want to display, to use messages you have to import it first
        return redirect("/login")
    return render(request, "htmlsss/register.html", context={"firstname":[], "lastname":[], "username":[], "password":[]})

def logoutpage(request):
    if request.method=="GET":
        logout(request)
        return redirect("/login")


    
