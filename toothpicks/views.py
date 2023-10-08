from django.shortcuts import render,redirect
import webbrowser
from django.contrib import messages
from django.http import HttpResponseRedirect
from django import forms
from django.core.exceptions import ViewDoesNotExist

class RedirectException(BaseException):
    def __init__(self, url):
        self.url = url

form_data_list = []
class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField()
    email = forms.EmailField()
    phoneNumber = forms.CharField()
    product = forms.CharField()
    quantity = forms.CharField()
    message = forms.CharField()



def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def checkorders(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "Sheikh Hanfi" and password == "7bugstoothpicks":
            
            context = {
                'form_data_list': form_data_list,
            }
            print(context)
            return render(request,"orderslist.html",context)
        else:
            return render(request, "login.html")

 
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phoneNumber = request.POST['phone']
        message = request.POST['message']
        url =f"https://wa.me/923034139181?text=Name : {name}%0aPhone Number : {phoneNumber}%0aMessage : {message}"
        webbrowser.open(url)
        return render(request, 'retur.html')
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
        form = MyForm(request.POST)

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
        form_data_list.append(formdata)
        print(form_data_list)
        url =f"https://wa.me/923034139181?text=Name : {name}%0aEmail : {email}%0aPhone Number : {phoneNumber}%0aProduct : {product}%0aNumber of Box : {quantity}%0aMessage : {message}"
        webbrowser.open_new_tab(url)
        return render(request, "order.html")
        

   