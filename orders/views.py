from django.shortcuts import render,redirect,get_object_or_404
from .models import Order,OrderItem
from .forms import OrderCreatedForm
from cart.cart import Cart
from .tasks import order_created
# Create your views here.


def order_create(request):
    cart = Cart(request)
    form = OrderCreatedForm()

    if request.method == 'POST':
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price= item['price'],
                                                            quantity = item['quantity'])

            #cart clear
            cart.clear()
            order_created.delay(order.id)
            return render(request,'orders/created_yes.html',{'order':order,'form':form})
        else:
            form = OrderCreatedForm()
    return render(request,'orders/create.html',{'cart':cart, 'form':form})

