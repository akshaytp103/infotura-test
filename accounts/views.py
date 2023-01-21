from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'test.html')

def register(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(2222222111111)
        if form.is_valid():
            
            print(55555555)
            email      = form.cleaned_data['email']
            mobile     = form.cleaned_data['mobile']
            faculty     = form.cleaned_data['faculty']
            password   = form.cleaned_data['password']
           
            user = Account.objects.create_user(
                 
                 email         = email,
                 mobile      = mobile,
                 faculty      =faculty,
                 password      = password
            )
            
            user.save()

            
            
            print(11111111)
            if faculty == 'TEACHER':
                return redirect('applications_teacher')
            return redirect('applications')

    context = {'form' : form}
    print(3333333333)
    return render(request,'signup.html',context)




def applications(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid(): 
            address = form.save(commit=False)
            address.user_id = request.user.id
            address.save()
            return redirect('home')
    else:
        form = AddressForm()
    return render(request, 'home.html', {'form': form})


def applications_teacher(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid(): 
            address = form.save(commit=False)
            address.user_id = request.user.id
            address.save()
            return redirect('home')
    else:
        form = AddressForm()
    return render(request, 'home2.html', {'form': form})