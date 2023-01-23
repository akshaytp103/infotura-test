from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('applications/',views.applications,name='applications'),
    path('applications/teacher/',views.applications_teacher,name='applications_teacher'),
    path('logout/',views.logout,name='logout'),
]
