from django.shortcuts import render

def home_page(request):
    context = {
        "title":"Home",
        "content":"Welcome to the home page"
    }
    return render(request, 'home.html', context)

def contact_page(request):
    context = {
        "title":"Home",
        "content":"Welcome to the contact page"
    }
    if request.method == "POST":
        print(request.POST.get("full_name"))
    return render(request, 'contact.html', context)
