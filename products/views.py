#Django
from django.shortcuts import render

#Models
from products.models import Product
""" products = [
    {
        'name': 'Pollo',
        'value': 26000,
        'active': False,
        'image': ''
    },
    {
        'name': 'Hamburguesa',
        'value': 10000,
        'active': True,
        'image': ''
    },
    {
        'name': 'Perro Caliente',
        'value': 6000,
        'active': True,
        'image': ''
    },
] """

# Create your views here.
def list_products(request):
    #products = ['Pollo', 'Hamburguesa', 'Perro Caliente']
    products = Product.objects.all()
    return render(
        request, 
        'products/products.html',
        {
            'title': 'Productos de la Carta',
            'description': 'Aqui presentaremos los productos de la carta',
            'products': products
        }
    )

def create_product(request):
    if request.method == "POST":
        #crear un nuevo producto
        new_product = Product(
            code=request.POST['code'],
            name=request.POST['name'],
            description=request.POST['description'],
            value=request.POST['value'],
        )
        new_product.save()
    return render(
        request=request,
        template_name='products/create_product.html'
    )