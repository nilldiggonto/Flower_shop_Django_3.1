from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',include('cart.urls',namespace='cart')),
    path('create/',include('orders.urls',namespace='orders')),
    path('coupon/',include('coupons.urls',namespace='coupons')),
    path('',include('shop.urls', namespace='shop')),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
