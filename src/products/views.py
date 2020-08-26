from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        #confirming delete
        obj.delete()
        return redirect('../')

    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'title': 'Awesome Title'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    # form = RawProductForm(request.POST or None, initial=initial_data)

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



# def product_create_view(request):    # Raw Form
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, "product/detail.html", context)
