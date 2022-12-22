from django import forms
from django.forms import PasswordInput
from .models import Item, AppUser

class ItemCreateForm(forms.ModelForm):
    class Meta:
        fields = ("title", "category", "particular", \
            "ledger_folio", "quantity", "price")
        model = Item

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        fields = ("email", "password")
        model = AppUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        fields = "__all__"
        model = AppUser