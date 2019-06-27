from django.urls import path
from product import views

urlpatterns = [
    path('shop/', views.showProductsInShopPage, name='shop'),
    path('product-detail/<int:productId>', views.viewDetailsProduct, name='detail')
]
