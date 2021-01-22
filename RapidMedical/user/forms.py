from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, HospitalInfo




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class HospitalInfoForm(forms.ModelForm): 
#

    class Meta: 
        model = HospitalInfo
        fields = '__all__'


class HospitalProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = HospitalInfo
        fields = ['description','ValidDoc', 'Frontview', 'Backview',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','is_hospital','phoneNumber', 'location']







