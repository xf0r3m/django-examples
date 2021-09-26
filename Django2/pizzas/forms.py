from django import forms

from .models import Order

class NewOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza', 'size', 'sauce1', 'sauce2', 'deliver']
        labels = { 
            'pizza': 'Pizza', 
            'size': 'Wielkość',
            'sauce1': 'Pierwszy sos',
            'sauce2': 'Drugi sos',
            'deliver': 'Dostawa'
        }
        size_choice = [
            (None, '-----------'),
            ('S', 'Mała'), 
            ('M', 'Duża'),
            ('L', 'Familijna'),
            ('XL', 'XXL 55cm')
        ]
        sauce_choice = [
            ('br', '-----------'),
            ('k', 'Ketchup'),
            ('m', 'Majonez'),
            ('cz', 'Czosnkowy'),
            ('pik', 'Pikantny')
        ]
        deliver_choice = [
            (None, '-----------'),
            ('odb', 'Odbiór osobisty'),
            ('dwz', 'Dowóz')
        ]
        widgets = {
            'size': forms.Select(choices=size_choice),
            'sauce1': forms.Select(choices=sauce_choice),
            'sauce2': forms.Select(choices=sauce_choice),
            'deliver': forms.Select(choices=deliver_choice)
        }

