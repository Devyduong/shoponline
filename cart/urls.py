from django.urls import path
from cart import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add-to-my-cart/<int:productId>/<int:quantity>', views.addProductToCart, name='addToCart'),
    path('remove/<int:cartItemId>', views.removeCartItem, name='remove')
]