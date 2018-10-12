from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "form_full_name",
                "placeholder": "Your full name"
                }
                )
            )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "form_email",
                "placeholder": "Your email address"
                }
                )
            )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "form_email",
                "placeholder": "Your message"
                }
                )
            )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gamil.com" in email:
            raise forms.ValidationError("Your email must be a gmail!")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username"
                }
                )
            )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"
                }
                )
            )

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username"
                }
                )
            )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "form_email",
                "placeholder": "Enter your email address"
                }
                )
            )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"
                }
                )
            )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password again"
                }
                )
            )
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Password and Password Confirm should match")
        return data
