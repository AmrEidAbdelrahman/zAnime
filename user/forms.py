from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100'}
))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    location = forms.CharField(max_length=20)
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['pic' , 'location']
