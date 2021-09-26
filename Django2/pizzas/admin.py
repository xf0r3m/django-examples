from django.contrib import admin
from .models import Pizza,Toping,Order

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Toping)
admin.site.register(Order)