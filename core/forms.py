from django import forms
from .models import Customer, Product, Order, Category

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone', 'email']
# forms.py
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'quantity', 'status', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']