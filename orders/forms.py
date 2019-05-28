from django import forms
from .models import * 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('restaurant', 'max_user', 'min_price', 'delivery_price',)
        widgets = {
            'restaurant': forms.TextInput(label='음식점', attrs={
                'required': True,
            }),
            'max_user': forms.NumberInput(label='최대매칭인원', attrs={
                'max': '4',
                'min': '0',
            }),
            'min_price': forms.TextInput(label='최소금액', attrs={
                'required': True,
            }),
            'delivery_price': forms.CheckboxInput(label='배달비(optional)')
        }
    