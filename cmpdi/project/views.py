from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from project.models import Profile
from .models import RandomDetail
from django.contrib.auth.decorators import login_required

def index(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def Contact(request):
    return render (request, 'Contact.html')



def userlogin(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            error_message = "Invalid username or password."
    
    return render(request, "userlogin.html", {"error": error_message})


def account(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/admin")
        else:
            error_message = "Invalid username or password."
    
    return render(request, "custom_login.html", {"error":error_message})


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

@login_required
def random_detail_create(request):
    if request.method == 'POST':

        profile = Profile.objects.get(user=request.user)

        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        field3 = request.POST.get('field3')
        field4 = request.POST.get('field4')
        field5 = request.POST.get('field5')
        field6 = request.POST.get('field6') == 'on'  # Checkbox field
        field7 = request.POST.get('field7')
        field8 = request.POST.get('field8')
        field9 = request.POST.get('field9')
        field10 = request.POST.get('field10')

        random_detail = RandomDetail.objects.create(
            profile=profile,
            field1=field1,
            field2=field2,
            field3=field3,
            field4=field4,
            field5=field5,
            field6=field6,
            field7=field7,
            field8=field8,
            field9=field9,
            field10=field10
        )
        random_detail.save()
        return redirect('/')  # Redirect to a success page or another view
    
    return render(request, 'home.html')