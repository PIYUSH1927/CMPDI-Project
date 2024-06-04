from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from project.models import Profile

def index(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def Contact(request):
    return render (request, 'Contact.html')



def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            return render(request,"userlogin.html")
    
    return render(request, "userlogin.html")


def account(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/admin")
        else:
            return render(request,"custom_login.html")
    
    return render(request, "custom_login.html")


def userlogout(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        department_name = request.POST['department_name']
        department_id = request.POST['department_id']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            profile = Profile(user=user, department_name=department_name, department_id=department_id)
            profile.save()
            login(request,user)
            return redirect('/home')
    return render(request, 'register.html')

def home(request):
    if request.user.is_anonymous:
        return redirect("/userlogin")
    return render (request,"home.html")