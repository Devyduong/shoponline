from django.shortcuts import render, redirect
from django.contrib.auth import *
from datetime import datetime
from .models import Cart, CartItem
from user.models import CustomerUser
from product.models import Product

def cart(request):
    currentUserLogingInSystem = request.user.username
    if currentUserLogingInSystem == "":
        return redirect('/admin/login')
    else:
        getCurrentUserInfor = CustomerUser.objects.get(username = currentUserLogingInSystem)
        try:
            getCartByUserInfor = Cart.objects.get(user = getCurrentUserInfor)
        except:
            getCartByUserInfor = None

        if getCartByUserInfor is None:
            createCartForNewbie(currentUserLogingInSystem)
        else: 
            getCartByUserInfor = Cart.objects.get(user = getCurrentUserInfor)
            try:
                allCartItem = CartItem.objects.filter(cart = getCartByUserInfor)
                total = totalOrder(getCartByUserInfor.id)
            except:
                allCartItem = None
                total = totalOrder(getCartByUserInfor.id)
            return render(request,
                         'pages/cart.html',
                         {
                             'cart': getCartByUserInfor,
                             'cartItems': allCartItem,
                             'totalOrder': total
                         })
    return render(request,
                  'pages/cart.html',
                  {})

#auto create new cart if user didn't have any cart
def createCartForNewbie(currentUser):
    newbie = CustomerUser.objects.get(username = currentUser)
    newCart = Cart(user = newbie, created_at = datetime.now(), updated_at = datetime.now())
    try:
        newCart.save()
    except:
        return redirect('/admin/login')

#add Product to cart
def addProductToCart(request, productId, quantity):
    currentUserLogingInSystem = request.user.username
    getCurrentUserInfor = CustomerUser.objects.get(username = currentUserLogingInSystem)
    getCartByUserInfor = Cart.objects.get(user = getCurrentUserInfor)
    getProductById = Product.objects.get(id = productId)

    newCartItem = CartItem(cart = getCartByUserInfor, item = getProductById, quantity = quantity)
    newCartItem.save()
    return redirect('/cart/')

def totalOrder(cartId):
    cart = Cart.objects.get(id = cartId)
    cartItems = CartItem.objects.filter(cart = cart)
    total = 0
    for cartItem in cartItems: 
        total += cartItem.item.price
    return total