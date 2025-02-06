from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    category = request.GET.get('category', '')
    products = Product.objects.all()
    
    if category:
        products = products.filter(category__slug=category)
    
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'product_list.html', {'page_obj': page_obj})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})