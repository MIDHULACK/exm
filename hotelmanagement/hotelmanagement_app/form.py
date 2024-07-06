from django import forms
from django.contrib.auth.models import User
from hotelmanagement_app.models import HotelModel

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
             'last_name':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.EmailInput(attrs={'class':'form-control'}),
             'username':forms.TextInput(attrs={'class':'form-control'}),
             'password':forms.TextInput(attrs={'class':'form-control'})
        
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']      
        widget={'username':forms.TextInput(attrs={'class':'form-control'}),
                'password':forms.TextInput(attrs={'class':'form-control'})
                }
class HotelForm(forms.ModelForm):
    class Meta:
        model=HotelModel
        fields=['Name','email','status']      
        widget={'Name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'status':forms.TextInput(attrs={'class':'form-control'}),
                }        
class EditForm(forms.ModelForm):
    class Meta:
        model=HotelModel
        fields=['Name','email','status']      
        widget={'Name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'status':forms.TextInput(attrs={'class':'form-control'}),
                }           