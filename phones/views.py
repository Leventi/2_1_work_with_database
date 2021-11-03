from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort_param_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }

    sort_param = request.GET.get('sort', 'name')

    if sort_param:
        sort_param = sort_param_dict[sort_param]

    context = {
        'phones': Phone.objects.all().order_by(sort_param),
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': get_object_or_404(Phone, slug=slug)
    }
    return render(request, template, context)
