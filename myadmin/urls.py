from django.urls import path
from. import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),   
    path('agencies/', views.agencies, name="agencies"),  
    path('customer_profile/<int:id>/', views.customer_profile, name="customer_profile"),  
    path('customer/', views.customer, name="customer"),  
    path('myadmin_login/', views.myadmin_login, name="myadmin_login"),  
    path('login_check/', views.login_check, name="login_check"), 
    path('logout/', views.logout, name="logout"),  
    path('order_details/<int:id>/', views.order_details, name="order_details"),  
    path('orders/', views.orders, name="orders"),  
    path('profile/<int:id>/', views.profile, name="profile"),  
    path('view_agency/', views.view_agency, name="view_agency"),  
    path('view_feedback/', views.view_feedback, name="view_feedback"),  
    path('view_inquiry/', views.view_inquiry, name="view_inquiry"),  
    path('myadmin_change_password/', views.myadmin_change_password, name="myadmin_change_password"),  

    # ------------ State --------------
    path('add_state/', views.add_state, name="add_state"),
    path('edit_state/<int:id>/', views.edit_state, name="edit_state"),
    path('update_state/<int:id>/', views.update_state, name="update_state"),
    path('view_state/', views.view_state, name="view_state"),
    path('delete_state/<int:id>/', views.delete_state, name="delete_state"),

    # ------------ City --------------
    path('add_city/', views.add_city, name="add_city"),
    path('edit_city/<int:id>/', views.edit_city, name="edit_city"),
    path('update_city/<int:id>/', views.update_city, name="update_city"),
    path('view_city/', views.view_city, name="view_city"),
    path('delete_city/<int:id>/', views.delete_city, name="delete_city"),

    # ------------ Area --------------
    path('add_area/', views.add_area, name="add_area"),
    path('edit_area/<int:id>/', views.edit_area, name="edit_area"),
    path('update_area/<int:id>/', views.update_area, name="update_area"),
    path('view_area/', views.view_area, name="view_area"),
    path('delete_area/<int:id>/', views.delete_area, name="delete_area"),
]
