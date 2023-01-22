from django.shortcuts import render
from .models import *
from accounts.models import *
# Create your views here.

def timetable(request):
    profile = Profile.objects.all()
    department=DEPARTMENT.objects.all()
    teacher=Teacher.objects.all()
    context={
        'profile': profile,
        'department': department,
        'teacher': teacher
    }
    print(profile,department,teacher)
    return render(request, 'timetable.html',context)