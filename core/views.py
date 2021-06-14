from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.
def home(request):
    context ={'home':'active'}
    return render(request,'core/home.html',context)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        if len(name)<2 or len(email)<4:
            messages.error(request,'Please fill correctly')
        else:
            contact = Contact(name=name,email=email,content=content)
            contact.save()
            messages.success(request, 'You have sucessfully submitted')
    context = {'contact':'active'}
    return render(request,'core/contact.html',context)