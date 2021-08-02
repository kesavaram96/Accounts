from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"Login.html")

def home(request):
    return render(request,"Home.html")

def signout(request):
    return render