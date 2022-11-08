from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

# Create your views here.

# Create your views here.
from django.utils import timezone

from order.forms import OrderForm
from order.models import Order


def index(request):
    return render(request, 'buying/index.html')


@login_required(login_url='/login/')
def addOrder(request):
    if request.method == 'POST':
        order = OrderForm(request.POST)
        if order.is_valid():
            order = order.save(commit=False)
            #order.author = request.user tutaj trzeba wyciagnac z produktu autora
            order.create_time = timezone.now()
            order.last_edit_time = timezone.now()
            order.user = request.user
            order.save()
            return redirect('index')
        else:
            context = {'form': order}
            return render(request, 'buying/add.html', context)
    else:
        news = OrderForm()
        context = {'form': news}
        return render(request, 'buying/add.html', context)

def getAllOrders(request):
    order = Order.objects.order_by('-create_time')
    context = {'order': order}
    return render(request, 'buying/index.html', context)


def get(request, id):
    order = get_object_or_404(Order, id=id)
    context = {'order': order}
    return render(request, 'buying/get.html', context)

@login_required(login_url='/login/')
def delete(request, id):
   order = Order.objects.get(id=id)
   order.delete()
   return redirect('getAllOrders')


@login_required(login_url='/login/')
def edit(request, id):
    instance = Order.objects.get(id=id)
    form = OrderForm(request.POST or None, instance=instance)
    if form.is_valid():
          form = form.save(commit=False)
          form.last_edit_time = timezone.now()
          form.user = request.user
          form.save()
          return redirect('index')
    form.fields['name'].initial = instance
    return render(request, 'buying/edit.html', {'form': form})

