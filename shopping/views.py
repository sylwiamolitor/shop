from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import ProductForm
from .models import Product, Order


# Create your views here.
def index(request):
    return render(request, 'shopping/index.html')


@login_required(login_url='/login')
@staff_member_required(login_url='/login')
def addProduct(request):
    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product = product.save(commit=False)
            product.author = request.user
            product.create_time = timezone.now()
            product.last_edit_time = timezone.now()
            product.save()
            return redirect('index')
        else:
            context = {'form': product}
            return render(request, 'shopping/add.html', context)
    else:
        news = ProductForm()
        context = {'form': news}
        return render(request, 'shopping/add.html', context)

def getAllProducts(request):
    product = Product.objects.order_by('-create_time')
    context = {'product': product}
    return render(request, 'shopping/index.html', context)


def get(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'shopping/get.html', context)

@transaction.atomic
@permission_required('shopping.add_order', login_url="/login")
def buy(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if product.stock_number < quantity:
            context = {'product': product, 'error': 'The selected product quantity is not in stock!'}
            return render(request, 'shopping/get.html', context)

        product.stock_number -= quantity
        order = Order(
            user=get_user(request),
            product=product,
            quantity=quantity,
            price=product.price,
            create_time=timezone.now(),
            last_update_time=timezone.now()
        )

        product.save()
        order.save()

        context = {'order': order}
        return render(request, 'shopping/buy.html', context)
    else:
        context = {'product': product}
        return render(request, 'shopping/get.html', context)
