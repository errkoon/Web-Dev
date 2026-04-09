from django.http import JsonResponse
from .models import Product, Category


def products_list(request):
    products = Product.objects.all()
    
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price
        })
    return JsonResponse(data, safe=False)


def product_detail(request, id):
    p = Product.objects.get(id=id)
    return JsonResponse({
        'id': p.id,
        'name': p.name,
        'price': p.price
    })


def categories_list(request):
    categories = Category.objects.all()
    data = []
    for c in categories:
        data.append({
            'id': c.id,
            'name': c.name
        })
    return JsonResponse(data, safe=False)


def category_detail(request, id):
    c = Category.objects.get(id=id)
    return JsonResponse({
        'id': c.id,
        'name': c.name
    })


def products_by_category(request, id):
    products = Product.objects.filter(category_id=id)
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name
        })
    return JsonResponse(data, safe=False)