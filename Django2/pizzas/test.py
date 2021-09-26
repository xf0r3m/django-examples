
from pizzas.models import Pizza,Toping
    
pizzas = Pizza.objects.all()

context=[]

class PizzaClass():
    def __init__(self, name, topings):
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
    p = PizzaClass(pizza_name, t)
    context.append(p)

class Order(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    sauce1 = models.CharField(max_length=10)
    sauce2 = models.CharField(max_length=10)
    deliver = models.CharField(max_length=10)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pizza.name} - {self.size},{self.sauce1},\
        {self.sauce2},{self.deliver}"