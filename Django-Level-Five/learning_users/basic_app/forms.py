from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        # fields = ('username', 'email', 'password', 'first_name', 'last_name')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
        # fields = ('portfolio_site', 'profile_pic', 'first_name', 'last_name')