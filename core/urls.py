from django.urls import path
from . import views
from .views import CustomerCreateView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'core'

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'), 
    
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),  # This was missing
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    
    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Order URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    
    
    

    
]
