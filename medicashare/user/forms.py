from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=30)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='last name')
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='confirm password', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("password doesn't match")
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if  not cd['username'].isalnum():
            raise forms.ValidationError('username must starts with a least 3 letters ')
        elif User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('username exists')
        return cd['username']
    # def clean_email(self):
    #     cd = self.cleaned_data
    #     if User.objects.filter(email=cd['email']).exists():
    #         raise forms.ValidationError('email already taken ')
    #     return cd['email']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='fname')
    last_name = forms.CharField(label='sname')

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
    def clean_first_name(self):
        cd = self.cleaned_data
        if not cd['first_name'].isalpha():
            raise forms.ValidationError('please enter a valid name')
        return cd['first_name']
    def clean_last_name(self):
        cd = self.cleaned_data
        if not cd['last_name'].isalpha():
            raise forms.ValidationError('please enter a valid name')
        return cd['last_name']  

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image','phone_number')