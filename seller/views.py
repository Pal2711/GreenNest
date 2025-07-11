from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from .forms import *

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def index(request):
    if "username" not in request.session:
        return redirect("login")
    
    mainitemlist = mainitem.objects.all()
    return render(request, 'index.html', {'mainitemlist': mainitemlist})

def crops(request):
    cropsdata = mainitem.objects.all()
    return render(request, 'crops.html', {'cropsdata': cropsdata})

def about(request):
    return render(request, 'about.html')

def Request(request):
    if request.method == "POST":
        form = requesstfomr(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data.get('your_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            send_mail(
                subject=f'New Feedback from {name}',
                message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email='your_email@gmail.com',
                recipient_list=['your_email@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "Thank you for your feedback!")
            return redirect("Request")
        else:
            print(form.errors)

    return render(request, 'Request.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup DONE")
            return redirect("login") 
        else:   
            print(form.errors)
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        um = request.POST.get("username")
        pa = request.POST.get("password")

        # Correct field names (case-sensitive)
        user = Signup.objects.filter(username=um, password=pa).first()

        if user:
            print("Login Successful!!")
            request.session["username"] = um  # Save session
            return redirect("index")  # Change to your desired redirect page
        else:
            print("Error! Login failed...")

    return render(request, "login.html")

def logout(request):
    if "username" in request.session:
        del request.session["username"]
    return redirect("index")  # Redirect to login page


def sell(request):
    if request.method == "POST":
        sell = sellproductform(request.POST,request.FILES)
        if sell.is_valid():
            sell.save()
            print("youre item is listed")
            return redirect ("index")
        else:
            print(sell.errors)

    return render(request, 'sell.html')

def firut(request):
    firutdata = Firut.objects.all()
    return render(request, "firut.html", {"firutdata": firutdata})

def Vege(request):
    Vegetablesdata = Vegetables.objects.all()
    return render(request, "vege.html", {"Vegetablesdata": Vegetablesdata})