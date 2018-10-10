from django import forms

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
