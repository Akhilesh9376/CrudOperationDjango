from django import forms
from App1.models import User
from django.core import validators


class studentRegistration(forms.ModelForm):
    class Meta:
        model=User
        # name=forms.charfield(validators=[validators.MaxLengthValidator(10)])
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name','required':'Please Fill Your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email','required':'PLease fill Your Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'})
        }
        # validation error for name (special )
        # def clean_name(self):
        #     val_name=self.cleaned_data['name']
        #     if len(val_name)<4:
        #         raise forms.ValidationError("Enter More than 4 Caracters ")
        #     return val_name


        # def clean(self):
        #     cleaned_data=super().clean()
        #     val_name=self.cleaned_data=['name']
        #     val_email=self.cleaned_data['email']
        #     if len(val_name)<4:
        #         raise forms.ValidationError('Name SXhould be more than or equla to 4')
        #     if len(val_email)<10:
        #         raise forms.ValidationError("Email Should be more than or equal to 10")


            
