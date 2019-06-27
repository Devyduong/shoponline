from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product

#Product's functions and methods===============================================================================================

#get all products and paginator 
#url /shop/
def showProductsInShopPage(request):
    numberProductsPerPage = 4
    getAllProducts = Product.objects.all()
    paginator = Paginator(getAllProducts, numberProductsPerPage)
    page = request.GET.get('page')
    try:
        allProducts = paginator.page(page)
    except PageNotAnInteger:
        allProducts = paginator.page(1)
    except EmptyPage:
        allProducts = paginator.page(paginator.num_pages)


    return render(request, 
                  'pages/shop.html', 
                  {
                    'allProducts': allProducts,
                    'totalProducts': getAllProducts.count(),
                  })

#show product details by id
#url product-detail/<int:productId>
def viewDetailsProduct(request, productId):
    getProductById = Product.objects.get(id = productId)
    return render(request,
                 'pages/product.html',
                 {
                    'productDetailById' : getProductById,   
                 })
#================================================================================================Product's functions and methods
