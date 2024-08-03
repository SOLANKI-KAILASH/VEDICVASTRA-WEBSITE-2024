from django.shortcuts import render,redirect,HttpResponseRedirect
from home.models import ContactModel,AddressModel,PaymentModel
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        contact=ContactModel(firstname=firstname,lastname=lastname,email=email,phone=phone,message=message)
        contact.save()
        return HttpResponseRedirect("/contactsuccess")
    return render(request,"contact.html")
def traditional(request):
    return render(request,"traditional.html")
def cultural(request):
    return render(request,"cultural.html")
def ocassional(request):
    return render(request,"ocassional.html")
def address(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state=request.POST.get("state")
        zip=request.POST.get("zip")
        address=AddressModel(name=name,email=email,address=address,city=city,state=state,zip=zip)
        address.save()
        return HttpResponseRedirect("/payment")
    return render(request,"address.html")

def payment(request):
    if request.method=="POST":
        name=request.POST.get("name")
        number=request.POST.get("number")
        expiration=request.POST.get("expiration")
        cvv=request.POST.get("cvv")
        payment=PaymentModel(name=name,number=number,expiration=expiration,cvv=cvv)
        payment.save()
        return HttpResponseRedirect("/successful")
    return render(request,"payment.html")

def successful(request):
    return render(request,"successful.html")

def status(request):
    return render(request,"status.html")

def contactsuccess(request):
    return render(request,"contactsuccess.html")
