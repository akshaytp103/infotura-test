from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser
# Create your models here.

 
class AccountManager(BaseUserManager):
    def create_user(self,email,mobile,faculty,password=None,is_staff=False):
        if not email:
            raise ValueError('must provide an email')
        if not mobile:
            raise ValueError('must provide a number')
        
        user=self.model(
            email       =  self.normalize_email(email),
            mobile      =  mobile,
            faculty     =faculty,
              
                 
        )
        user.is_active       = True
        user.is_staff        = True
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,mobile,faculty,password):
        user = self.create_user(
            email        = self.normalize_email(email),
            mobile       = mobile,
            faculty     = faculty,
            password     = password,
                  
        )
        user.is_admin        = True
        user.is_active       = True
        user.is_staff        = True
        user.is_superadmin   = True
        user.save   (using=self._db)
        return user



  
class Account(AbstractBaseUser):
    facultytypes =(
    ('COUNSELLOR','COUNSELLOR'),
    ('RESEARCH ASSISTANT','RESEARCH ASSISTANT'),
    ('GRAPHIC DESIGNER','GRAPHIC DESIGNER'),
    ('WEBDEVELOPER','WEBDEVELOPER'),
    ('TEACHER','TEACHER'),
    ('ACCOUNTANT','ACCOUNTANT'),
    ('VIDEO EDITOR','VIDEO EDITOR'),
    ('MARKETING','MARKETING')
    )
    
    
    email           =models.EmailField(max_length=100,unique=True) 
    mobile          =models.CharField(max_length=10,unique=True,null=True)
    is_admin        =models.BooleanField(default=False)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_superadmin   =models.BooleanField(default=False)
    faculty         =models.CharField(choices=facultytypes,null=True,blank=True,max_length=50)
    has_profile    =models.BooleanField(default=False)
    
    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS =['faculty','mobile']
    
    objects=AccountManager()

    

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True


class Profile(models.Model) :
    
    education_type=(
        ('sslc','sslc'),
        ('plustwo','plustwo'),
        ('degree','degree'),
        ('pg','pg'),
        ('BEd','BEd'),
        ('phd','phd')
    )

    experience_type=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    
    name            =models.CharField(max_length=50) 
    user = models.ForeignKey(Account, on_delete=models.CASCADE)   
    address=models.CharField(max_length=200) 
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pin_code = models.CharField(max_length=6)
    mobile=models.CharField(max_length=15)
    Education       = models.CharField(max_length=50,choices=education_type)
    experience=models.CharField(max_length=10,choices=experience_type)
    created_at = models.DateTimeField(auto_now_add=True) 
        
    class Meta :
        verbose_name = 'Profile'
        verbose_name_plural = "Profile"
        
    def __str__(self) :
        return self.name
    
    
  
class DEPARTMENT(models.Model):
    dep_type =(
    ('psc','psc'),
    ('ssc','ssc'),
    ('bank','bank'),
    ('ugc','ugc'),
    ('net','net')
) 
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    department=models.CharField(max_length=50,choices=dep_type)
    
    def __str__(self) :
        return self.profile.name
    

class Subject(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Teacher(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    
    def __str__(self) :
        return self.profile.name