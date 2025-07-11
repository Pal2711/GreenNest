from django.shortcuts import render,get_object_or_404,redirect
from seller.models import sellproduct 
from .forms import *
from .models import *
from seller.models import sellproduct
from django.contrib.auth import logout 


def buyreindex(request):
    if "user" not in request.session:
        return redirect("buyerlogin")
    
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(sellproduct, id=product_id)
        product.delete()  # Simulate "buy" by deleting
        return redirect("buyreindex") 
    
    byeitem = sellproduct.objects.all()

    return render(request, "buyreindex.html",{'byeitem': byeitem})

def product_detail(request, id):
    product = get_object_or_404(sellproduct, id=id)
    return render(request, 'product_detail.html', {'product': product})

def buyreabout(request):
    return render(request,"buyreabout.html")

def buyrecontact(request):


    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            print("Thank you for contacting us")
            return redirect("buyrecontact")
        else:
            print(form.errors) 
    return render(request,"buyrecontact.html")

def buyerlogin(request):
    if request.method == "POST":
        um = request.POST.get("name")
        pas = request.POST.get("Password")

        user = usersgimup.objects.filter(name=um, Password=pas).first()
        if user:
            print("Login Successful!!")
            request.session["user"] = um
            return redirect("buyreindex")
        else:
            print("Error! Login failed...")

    return render(request, "buyerlogin.html")

def buyer_logout(request):
    if "user" in request.session:
        del request.session["user"]
    return redirect("buyerlogin")

def buyersginup(request):
    if request.method == "POST":
        form = sginupform(request.POST)
        if form.is_valid():
            form.save()
            print("thank you for sginup")
            return redirect("buyerlogin")
        else:
            print(form.errors)
    return render(request,"buyersginup.html")
