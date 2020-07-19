from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
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

class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    #as we don't see context data in CBV we will do this to get our contenxt data in CBV
    def get_context_data(self, *args, **kwargs):
        context =  super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        print(instance)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance

def product_detail_view(request,pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk = pk)#id
    #instance = get_object_or_404(Product, pk=pk)
    # alter nate to get_object_404
    # try:
    #     instance = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     raise Http404("product does not exist")
    # except:
    #     print("huh??")

    # alternate to get_object_404
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("product doesn't exist")
    # with model manager

    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("product doesn't exist")
    context = {
        'object' : instance
    }
    return render(request, "products/detail.html", context)
