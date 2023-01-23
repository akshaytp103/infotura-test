from django.shortcuts import render
from .models import *
from accounts.models import *
# Create your views here.

def timetable(request):
    timetable = Timetable.objects.all()
    context={
        'timetable' :  timetable,
    }
    
    return render(request, 'timetable.html',context)