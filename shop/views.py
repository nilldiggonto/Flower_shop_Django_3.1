from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Product, Category
# Create your views here.

## Product_category 
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)

    if category_slug:
        categories = get_object_or_404(Category,slug= category_slug)
        products = Product.filter(category=category)
    
    template_name = 'shop/product/list.html'
    context = {
        'category':category,
        'categories': categories,
        'products': products,
    }
    return render(request,template_name,context)

