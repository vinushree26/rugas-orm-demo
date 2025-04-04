from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    
    
    def save(self, *args, **kwargs):
        # Delete old image when updating
        try:
            old = Product.objects.get(pk=self.pk)
            if old.image != self.image:
                old.image.delete(save=False)
        except Product.DoesNotExist:
            pass
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list')
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        editable=False
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer_list')

ORDER_STATUS = (
    ('placed', 'Placed'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='placed')
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"

    def get_absolute_url(self):
        return reverse('order_list')

    def total_price(self):
        return self.quantity * self.product.price