from django import forms
from ._base_form import BaseForm
from .util import TextInput, PasswordInput, Select

class LoginForm(forms.Form):
    username = forms.EmailField(label="Email", widget=TextInput(attrs={"autocomplete": "email"}))
    password = forms.CharField(label="Password", widget=PasswordInput(attrs={"autocomplete": "current-password"}))

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=TextInput(attrs={"autocomplete": "first-name"}))
    last_name = forms.CharField(label="Last Name", widget=TextInput())
    email = forms.EmailField(label="Email", widget=TextInput())
    password = forms.CharField(label="Password", widget=PasswordInput())
    password_confirmation = forms.CharField(label="Confirm Password", widget=PasswordInput())
    family = forms.ChoiceField(label="Family", widget=Select(), choices=[["new", "New Family"], ["bob", "Bob's Family"]])
