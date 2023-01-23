from django.db import models
from accounts.models import Subject,Teacher

# Create your models here.

class quarter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f'{self.subject.name}+{self.teacher}'
    

    
class Timetable(models.Model):
    days=(
        ('MONDAY','MONDAY'),
        ('TUESDAY','TUESDAY'),
        ('WEDNESDAY','WEDNESDAY'),
        ('THURSDAY','THURSDAY'),
        ('FRIDAY','FRIDAY'),
        ('SATURDAY','SATURDAY'),
        ('SUNDAY','SUNDAY'),
    )
    date = models.CharField(max_length=20,choices=days)
    quarter_1 = models.ForeignKey(quarter,null=True,blank=True,on_delete=models.CASCADE,related_name='quarter_1_quarter')
    quarter_2 = models.ForeignKey(quarter,null=True,blank=True,on_delete=models.CASCADE,related_name='quarter_2_quarter')
    quarter_3 = models.ForeignKey(quarter,null=True,blank=True,on_delete=models.CASCADE,related_name='quarter_3_quarter')
    quarter_4 = models.ForeignKey(quarter,null=True,blank=True,on_delete=models.CASCADE,related_name='quarter_4_quarter')
    
    def __str__(self):
        return str(self.date)