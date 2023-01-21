from django import forms
from django.forms import fields    
from . models import *

class RegistrationForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Account
        fields=['email','mobile','faculty','password']
        

    def __init__(self,*args,**kwargs):
        super(RegistrationForm ,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data    =super(RegistrationForm,self).clean()
        password        =cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user 

class AddressForm(forms.ModelForm) :
    class Meta :
        model = Profile
        fields =['name','address','state','country','pin_code','Education','experience','mobile']
        

    def __init__(self, *args, **kwargs):
        super(AddressForm,self).__init__(*args, **kwargs)

        for field in self.fields :
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
            
    
        
   