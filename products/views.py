from django.shortcuts import render
from django.views.generic import ListView

from .models import Product
# importing class of model for searching against it

# Class based view
class ProductListView(ListView):
    queryset = Product.objects.all()
    # grabs everything from Product table of database
    template_name = "products/list-cbv.html"


# Function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {'qs': queryset}
    return render(request, "products/list-fbv.html", context)
