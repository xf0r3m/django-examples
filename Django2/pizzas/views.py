from django.shortcuts import render, redirect
from .forms import NewOrder
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def menu(request):

    from pizzas.models import Pizza,Toping
    
    pizzas = Pizza.objects.all()

    p={}
    context=[]

    class PizzaClass():
        def __init__(self, id, name, topings):
            self.id = id
            self.name = name
            self.topings = topings

    for pizza in pizzas:
        pizza_name = f"{pizza}"
        topings = pizza.toping_set.all()
        t=""
        for toping in topings:
            if len(t) == 0:
                t=f"{toping}, "
            else:
                t=f"{t}{toping}, "
        t=t.rstrip(', ')
        p1 = PizzaClass(pizza.id, pizza_name, t)
        context.append(p1)

    p['pizzas']=context

    return render(request, 'pizzas/menu.html', p)

def pizza_site(request, pizza_id):

    from pizzas.models import Pizza,Toping

    context = {}

    name = Pizza.objects.get(id=pizza_id)
    topings = name.toping_set.all()

    context['name'] = name
    context['topings'] = topings

    return render(request, 'pizzas/pizza_site.html', context)

@login_required
def orders_view(request):

    from pizzas.models import Order

    if request.user.username != 'pizza_admin':
        orders = Order.objects.filter(owner=request.user).order_by('-date_order')
    else:
        orders = Order.objects.order_by('-date_order')


    context = {'orders': orders}
    return render(request, 'pizzas/orders_view.html', context)

@login_required
def new_order(request):

    if request.method != 'POST':
        form = NewOrder()
    else:
        form = NewOrder(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.owner = request.user
            new_order.save()
            return redirect('pizzas:index')
    context = {'form': form}
    return render(request, 'pizzas/new_order.html', context)

@login_required
def edit_order(request, order_id):

    if request.user.username != 'pizza_admin':
        raise Http404

    from .models import Order

    order = Order.objects.get(id=order_id)

    if request.method != 'POST':
        form = NewOrder(instance=order)
    else:
        form = NewOrder(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:index')
    context = {'form': form, 'order': order}
    return render(request, 'pizzas/edit_order.html', context)    

