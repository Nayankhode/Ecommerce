from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    #as we don't see context data in CBV we will do this to get our contenxt data in CBV
    def get_context_data(self, *args, **kwargs):
        context =  super(ProductListView, self).get_context_data(*args, **kwargs)
        # to add extra query set if we need for class based view
        # abc = Product.objects.all()
        # context['abc'] = abc
        print(context)
        return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "products/list.html", context)