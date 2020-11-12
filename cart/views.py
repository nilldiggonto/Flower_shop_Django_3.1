from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.

##### ADD
@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity = cd['quantity'], override_quantity= cd['override'])

    return redirect('cart:cart_detail')


##### DELETE

@require_POST
def cart_delete(request,product_id):
    cart = Cart(request)

    Product = get_object_or_404(Product, id = product_id)

    cart.remove(product)

    return redirect('cart:cart_detail')



#### Cart Template
def cart_detail(request):
    cart = Cart(request)

    return render(request,'cart/detail.html',{'cart':cart})