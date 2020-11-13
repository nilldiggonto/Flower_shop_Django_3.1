from django.shortcuts import render,redirect,get_object_or_404
from .models import Order,OrderItem
from .forms import OrderCreatedForm
from cart.cart import Cart
# Create your views here.


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price= item['price'],
                                                            quantity = item['quantity'])

            #cart clear
            cart.clear()
            return render(request,'orders/create.html',{'cart':cart,'form':form})
        else:
            form = OrderCreatedForm()
    return render(request,'orders/create.html',{'cart':cart, 'form':form})

