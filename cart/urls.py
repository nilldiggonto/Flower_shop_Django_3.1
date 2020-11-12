from djanog.urls import path
from .views import cart_add,cart_delete,cart_detail

app_name = 'cart'

urlpatterns = [
    path('',cart_detail,name='cart_detail'),
    path('add/<int:product_id/',cart_add , name='cart_add'),
    path('remove/<int:product_id/',cart_delete,name='cart_remove'),
]