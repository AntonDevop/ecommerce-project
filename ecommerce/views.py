from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
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

def login_page(request):
    login_form = forms.LoginForm(request.POST or None)
    context = {
        "title":"Login",
        "content":"Welcome to the login page",
        "form": login_form,
        "error": ''
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context["error"] = "There is no such user!"
            return render(request,  "auth/login.html", context)

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    register_form = forms.RegisterForm(request.POST or None)
    context = {
        "title":"Register",
        "content":"Welcome to the login page",
        "form": register_form
    }
    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        password_confirm = register_form.cleaned_data.get("password_confirm")
        new_user = User.objects.create_user(username, email, password)

    return render(request, "auth/register.html", context)
