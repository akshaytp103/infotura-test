from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages,auth
from django.contrib.auth import authenticate, logout
# Create your views here.



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
            
            return redirect('login')

    context = {'form' : form}
    print(3333333333)
    return render(request,'signup.html',context)

def login(request):
    if request.user.is_authenticated:
        if request.user.has_profile:
            return redirect('timetable')
        # else:
        #     if request.user.faculty == 'TEACHER':
        #         return redirect('applications_teacher')
        #     return redirect('applications')

    if request.method == "POST":
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Account.objects.get(email=email)
        except :
            messages.error(request,"user Does not exist..")

        user = authenticate(request,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            if request.user.faculty == 'TEACHER':
                return redirect('applications_teacher')
            return redirect('applications')
        else:
            messages.error(request,'user does not exist..')

    return render(request,'login.html')


def applications(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid(): 
            address = form.save(commit=False)
            address.user_id = request.user.id
            address.save()
            return redirect('timetable')
    else:
        form = AddressForm()
    return render(request, 'home.html', {'form': form})




def applications_teacher(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            name      = form.cleaned_data['name']
            address     = form.cleaned_data['address']
            state     = form.cleaned_data['state']
            country   = form.cleaned_data['country']
            pin_code     = form.cleaned_data['pin_code']
            mobile   = form.cleaned_data['mobile']
            Education     = form.cleaned_data['Education']
            experience   = form.cleaned_data['experience']
            department     = form.cleaned_data['department']
            subject   = form.cleaned_data['subject']
           
            profile = Profile.objects.create(
                 user       =request.user,
                 name         = name,
                 address      = address,
                 state          =state,
                 country      = country,
                 pin_code        = pin_code,
                 mobile        = mobile,
                 Education      =Education,
                 experience      = experience
            )
            profile.save()
            department =DEPARTMENT.objects.create(
                profile       =profile,
                department = department,
            )
            subject =Teacher.objects.create(
                profile =profile,
                subject = subject,
            )
            department.save()
            subject.save()
            
            return redirect('timetable')
    else:
        form = ProfileForm()
    return render(request, 'home2.html', {'form': form})


def logout(request):
    return redirect('login')