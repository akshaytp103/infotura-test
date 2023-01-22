from django.db import models
from accounts.models import Subject,Teacher

# Create your models here.

class quarter(models.Model):
    starttime = models.TimeField()
    endtime = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f'{self.subject.name}+{self.teacher}'
    
class timesheet(models.Model):
    date = models.DateField(auto_now_add=True)
    quarter_1 = models.ManyToManyField(quarter,related_name='quarter_1_quarter')
    quarter_2 = models.ManyToManyField(quarter,related_name='quarter_2_quarter')
    quarter_3 = models.ManyToManyField(quarter,related_name='quarter_3_quarter')
    quarter_4 = models.ManyToManyField(quarter,related_name='quarter_4_quarter')
    
    def __str__(self):
        return str(self.date)