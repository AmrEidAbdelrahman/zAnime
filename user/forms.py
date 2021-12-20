from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100'}))


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    
    class Meta():
        model = Profile
        fields = ['location','pic']
        widgets = {'pic': forms.FileInput}
