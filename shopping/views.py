from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'shopping/index.html')


@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def delete(request, id):
   product = Product.objects.get(id=id)
   product.delete()
   return redirect('getAllProducts')


@login_required(login_url='/login/')
def edit(request, id):
    instance = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
          form = form.save(commit=False)
          form.last_edit_time = timezone.now()
          form.save()
          return redirect('index')
    form.fields['name'].initial = instance
    return render(request, 'shopping/edit.html', {'form': form})

