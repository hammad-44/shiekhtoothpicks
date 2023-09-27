from django.shortcuts import render,HttpResponse
from toothpicks.models import product,Contact, Order

# Create your views here.
def home(request):
    products= product.objects.all()
    context = {"products":products}
    return render(request, "home.html",  context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact=Contact(name=name, email=email, message=message)
        contact.save()
        return render(request, 'retur.html')
    else:
        return render(request,'contact.html')

def order(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        product = request.POST['product']
        quantity = request.POST['quantity']
        message = request.POST['message']
        order=Order(name=name, email=email,number=phoneNumber,product=product,quantity=quantity, message=message)
        order.save()
        return render(request, "order.html")
    else:
        return render(request,"home.html")