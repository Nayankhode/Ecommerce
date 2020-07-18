from django import forms
from django.contrib.auth import get_user_model
User = get_user_model

class LoginForm(forms.Form):
     userName =  forms.CharField()
     password =  forms.CharField(widget = forms.PasswordInput)

class RegisterForm(forms.Form):
     userName =  forms.CharField()
     email = forms.EmailField()
     password =  forms.CharField(widget = forms.PasswordInput)
     password2 = forms.CharField(label ="confirm password",widget=forms.PasswordInput)

     def clean_userName(self):
          userName = self.cleaned_data.get('userName')
          qs = User.objects.filter(username = userName)
          if qs.exists():
               raise forms.ValidationError("Username is taken")
          return userName

     def clean_email(self):
          email = self.cleaned_data.get('email')
          qs = User.objects.filter(email = email)
          if qs.exists():
               raise forms.ValidationError("email is taken")
          return email

     def clean(self):
          data = self.cleaned_data
          password = self.cleaned_data.get('password')
          password2 = self.cleaned_data.get('password2')
          if password2 != password:
               raise forms.ValidationError("Password must match")
          return data


