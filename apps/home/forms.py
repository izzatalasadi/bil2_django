"""
from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(validators=[EmailValidator()], required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class sellForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    files = forms.FileField(required=True)


class bookForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    car = forms.CharField(required=True)
    
"""