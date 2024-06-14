from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from project.models import Profile
from .models import Bill
from django.contrib.auth.decorators import login_required

def index(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def Contact(request):
    return render (request, 'Contact.html')

@login_required
def billview(request):
    try:
        profile = Profile.objects.get(user=request.user)
        bills = Bill.objects.filter(profile=profile)
    except Profile.DoesNotExist:
        return render(request, "billview.html")  

    if not bills:
        return render(request, "billview.html", {'bills': bills, 'message': 'No bills found.'})

    return render(request, "billview.html", {'bills': bills})

@login_required(login_url='/adminlogin')
def filter_bills(request):
    profile = Profile.objects.get(user=request.user)
    payment_status = request.GET.get('payment_status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    bills = Bill.objects.filter(profile__department_id=profile.department_id)

    if payment_status:
        bills = bills.filter(field9=payment_status)

    if start_date:
        bills = bills.filter(field4__gte=start_date)

    if end_date:
        bills = bills.filter(field4__lte=end_date)

    context = {
        'all_bills': bills
    }

    return render(request, 'adminview.html', context)


def userlogin(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/billview")
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



def adminlogin(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("/adminview")
            else:
                error_message = "You do not have the required permissions to access this page."
        else:
            error_message = "Invalid username or password."
    
    if request.user.is_authenticated:
        return render(request, "adminlogin.html")

    return render(request, "adminlogin.html", {'error_message': error_message})



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

@login_required(login_url='/adminlogin')
def adminview(request):
    if request.user.is_superuser:
        profile = Profile.objects.get(user=request.user)
        all_bills = Bill.objects.filter(profile__department_id=profile.department_id)
        return render(request, "adminview.html", {'all_bills': all_bills})
    else:
        return redirect("/adminlogin")



def update_status(request):
    if request.method == "POST":
        bill_id = request.POST.get("bill_id")
        payment_status = request.POST.get("payment_status")
        payment_date = request.POST.get("payment_date")

        try:
            bill = Bill.objects.get(id=bill_id)
            bill.field9 = payment_status
            bill.field10 = payment_date
            bill.save()
            return redirect('/adminview') 
        except Bill.DoesNotExist:
            return render(request, "error.html", {"message": "Bill does not exist."})

    return redirect('/adminview')




@login_required
def bills_detail_create(request):
    if request.method == 'POST':

        profile = Profile.objects.get(user=request.user)

        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        field3 = request.POST.get('field3')
        field4 = request.POST.get('field4')
        field41 = request.POST.get('field41')
        field5 = request.POST.get('field5')
        field6 = request.POST.get('field6') 
        field7 = request.POST.get('field7')
        field8 = request.POST.get('field8')
        field9 = request.POST.get('field9')
        field10 = request.POST.get('field10')
        field11 = request.FILES.get('field11')

        bill_detail = Bill.objects.create(
            profile=profile,
            field1=field1,
            field2=field2,
            field3=field3,
            field4=field4,
            field41=field41,
            field5=field5,
            field6=field6,
            field7=field7,
            field8=field8,
            field9=field9,
            field10=field10,
            field11=field11,
        )
        bill_detail.save()
        return redirect('/billview')  
    
    return render(request, 'home.html')

def update_payment_status(request):
    if request.method == 'POST':
        bill_id = request.POST.get('bill_id')
        payment_status = request.POST.get('payment_status')
        payment_date = request.POST.get('payment_date')
        
        # Update the bill object
        bill = Bill.objects.get(pk=bill_id)
        bill.field9 = payment_status
        bill.field10 = payment_date
        bill.save()

        return redirect('/billview')  
    else:
        return redirect('/billview') 