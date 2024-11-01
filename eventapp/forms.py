from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import eventModel, BookedUser, eventModel, EventCatorogy


class registrationForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(registrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': "Enter username",
            'class': 'mt-3 border border-primary p-2 user_input'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': "Enter email",
            'class': 'mt-3 border border-primary p-2 email_input'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': "Enter your password",
            'class': 'mt-3  border border-primary p-2 pass1_input'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': "Enter your confirm password",
            'class': 'mt-3 border border-primary p-2 pass2_input'
        }) 


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': "Username", 'class':'username_input border border-primary p-2'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': "Password", 'class':'password_input mt-3 mb-2 border border-primary p-2'}))


class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class eventForm(forms.ModelForm):
    class Meta:
        model = eventModel
        fields = '__all__'
        widgets = {
                    'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class':'border border-primary'})
                }
        
    widget=TextInput(attrs={'placeholder': "OTP", 'class':'rounded-1 p-2 custom-input border border-primary w-100'})


class BookedUser(forms.ModelForm):
    class Meta:
        model = BookedUser
        fields = '__all__'
        

class EventCatorogyForm(forms.ModelForm):
    class Meta:
        model = EventCatorogy
        fields = '__all__'