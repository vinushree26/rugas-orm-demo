from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Customer, Product, Order, Category
from .forms import CustomerForm, ProductForm, OrderForm, CategoryForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'core/customer_create.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Customer created successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('core:customer_list')

@login_required
def dashboard(request):
    total_customers = Customer.objects.filter(created_by=request.user).count()
    total_products = Product.objects.count()
    total_orders = Order.objects.filter(created_by=request.user).count()
    recent_orders = Order.objects.filter(created_by=request.user).order_by('-created_at')[:5]
    
    context = {
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'recent_orders': recent_orders,
    }
    return render(request, 'core/dashboard.html', context)

# Customer Views
@login_required
def customer_list(request):
    customers = Customer.objects.filter(created_by=request.user)
    return render(request, 'core/customer_list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.save()
            messages.success(request, 'Customer created successfully!')
            return redirect('core:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'core/customer_form.html', {'form': form})

@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully!')
            return redirect('core:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'core/customer_form.html', {'form': form})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk, created_by=request.user)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully!')
        return redirect('core:customer_list')
    return render(request, 'core/customer_confirm_delete.html', {'customer': customer})

# Product Views
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, 'Product created successfully!')
            return redirect('core:product_list')
    else:
        form = ProductForm()
    return render(request, 'core/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('core:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('core:product_list')
    return render(request, 'core/product_confirm_delete.html', {'product': product})

# Order Views
@login_required
def order_list(request):
    orders = Order.objects.filter(created_by=request.user).select_related('customer', 'product')
    return render(request, 'core/order_list.html', {'orders': orders})

@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user
            order.save()
            messages.success(request, 'Order created successfully!')
            return redirect('core:order_list')
    else:
        form = OrderForm()
    return render(request, 'core/order_form.html', {'form': form})

@login_required
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully!')
            return redirect('core:order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'core/order_form.html', {'form': form})

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk, created_by=request.user)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully!')
        return redirect('core:order_list')
    return render(request, 'core/order_confirm_delete.html', {'order': order})

# Category Views
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'core/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            messages.success(request, 'Category created successfully!')
            return redirect('core:category_list')
    else:
        form = CategoryForm()
    return render(request, 'core/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('core:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'core/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        if request.method == 'POST':
            category.delete()
            messages.success(request, 'Category deleted successfully!')
            return redirect('core:category_list')
        return render(request, 'core/category_confirm_delete.html', {'category': category})
    except Category.DoesNotExist:
        messages.error(request, 'Category does not exist!')
        return redirect('core:category_list')