from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "address",
            "city",
            "postal_code",
            "quantity",
            "total_amount",
        ]