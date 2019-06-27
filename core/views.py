from django.shortcuts import render
from product.models import Category

def index(request):
    getCategoriesForSearchBox = Category.objects.filter(active=True)
    return render(request, 'pages/index.html', { 
            'categoriesForSearchBox': getCategoriesForSearchBox,
        })
def contact(request):
    return render(request, 'pages/contact.html', {})