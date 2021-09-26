from django.urls import path

from . import views

app_name='pizzas'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('<int:pizza_id>', views.pizza_site, name='pizza_site'),
    path('orders/', views.orders_view, name="orders"),
    path('new_order/', views.new_order, name="new_order"),
    path('edit_order/<int:order_id>', views.edit_order, name='edit_order')
]