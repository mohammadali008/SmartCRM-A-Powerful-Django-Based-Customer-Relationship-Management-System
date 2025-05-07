from django import forms
from .models import *

# Define OrderForm
class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []
