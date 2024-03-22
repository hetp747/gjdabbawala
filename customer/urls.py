from django import views
from django.urls import path
from . import views

urlpatterns = [
    # ----------- Agency -----------------

    path('tiffin_register/', views.tiffin_register, name='tiffin_register'),

    # ----------- Customer -----------------
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),


    path('customer_home/', views.customer_home, name='customer_home'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:id>/', views.update_profile, name='update_profile'),
    path('customer_change_password/', views.customer_change_password, name='customer_change_password'),
    path('gallery/', views.gallery, name='gallery'),
    path('services_search/', views.services_search, name='services_search'),
    path('services/', views.services, name='services'),
    path('single/', views.single, name='single'),
    path('view_more_details/<int:id>/', views.view_more_details, name='view_more_details'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/', views.update_quantity, name="update_quantity"),
    path('order/', views.order, name='order'),
    path('success/', views.success, name='success'),
    path('customer_orders/', views.customer_orders, name='customer_orders'),
    path('customer_order_details/<int:id>/', views.customer_order_details, name='customer_order_details'),


]
