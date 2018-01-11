from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "fullname",
                "placeholder": "Your Full Name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Your email "
            }
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "subject",
                "placeholder": "Your Subject "
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "Your message "
            }
        )
    )
