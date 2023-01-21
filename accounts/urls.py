from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.register,name='register'),
    path('applications/',views.applications,name='applications'),
    path('application/teacher/',views.applications_teacher,name='applications_teacher'),
]
