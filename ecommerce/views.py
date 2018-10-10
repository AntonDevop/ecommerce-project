from django.shortcuts import render
from . import forms

def home_page(request):
    context = {
        "title":"Home",
        "content":"Welcome to the home page"
    }
    return render(request, 'home.html', context)

def contact_page(request):
    contact_form = forms.ContactForm(request.POST or None)
    context = {
        "title":"Home",
        "content":"Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data["email"])

    if request.method == "POST":
        name = request.POST.get("full_name")
        email = request.POST.get("email")
        content = request.POST.get("content")
    return render(request, 'contact.html', context)
