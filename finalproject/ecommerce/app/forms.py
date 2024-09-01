from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer



class LoginForm(AuthenticationForm):
    username = UsernameField(widget =forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'})),
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Old Password', widget = forms.PasswordInput(attrs={'autofocus':'True', 'autocomplete': 'current-password', 'class' : 'form-control'})),
    new_password1 = forms.CharField(label = 'New Password', widget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zip_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your locality'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your ZIP code'}),
        }

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label = 'New Password', widget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label = 'Confirm New password', widget = forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))