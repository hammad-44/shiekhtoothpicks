from django.shortcuts import render,redirect
from django.contrib import messages
from django import forms




def home(request):
    return render(request, "home.html")




 
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phoneNumber = request.POST['phone']
        message = request.POST['message']
        url =f"https://wa.me/923034139181?text=Name : {name}%0aPhone Number : {phoneNumber}%0aMessage : {message}"

        return redirect(url)
    else:
        return render(request,'contact.html')

def orderform(request):
    return render(request,'orderform.html')


def order(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        product = request.POST['product']
        quantity = request.POST['quantity']
        message = request.POST['message']

        if int(quantity) < 50 and product == "ToothPicks":
            messages.error(request,"You Have to Order Atleast 50 Boxes")
            return render(request, 'orderform.html')
        elif int(quantity) < 50 and product == "Printed ToothPicks":
            messages.error(request,"You Have to Order Atleast 50 Boxes")
            return render(request, 'orderform.html')
        elif int(quantity) < 10000 and product == "Sugar Sachets":
            messages.error(request,"You Have to Order Atleast 10,000 Pieces")
            return render(request, 'orderform.html')
        formdata = {"name":name,"email":email,"phoneNumber":phoneNumber,"product":product,"quantity":quantity,"message":message}
        url =f"https://wa.me/923034139181?text=Name : {name}%0aEmail : {email}%0aPhone Number : {phoneNumber}%0aProduct : {product}%0aNumber of Box : {quantity}%0aAdress : {message}"

        return redirect(url)
        

   