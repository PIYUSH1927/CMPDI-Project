from django.shortcuts import render

def index(request):
    return render (request, 'index.html')
def about(request):
    return render (request, 'about.html')
def Contact(request):
    return render (request, 'Contact.html')
def userlogin(request):
    return render (request, 'userlogin.html')