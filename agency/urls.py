from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('agency_dashboard/', views.agency_dashboard, name="agency_dashboard"),

    # ---------- Food ----------------
    path('add_food/', views.add_food, name="add_food"),
    path('edit_food/<int:id>/', views.edit_food, name="edit_food"),
    path('update_food/<int:id>/', views.update_food, name="update_food"),
    path('view_food/', views.view_food, name="view_food"),
    path('delete_food/<int:id>/', views.delete_food, name="delete_food"),

    # ------------ Food Category --------------
    path('add_foodcategory/', views.add_foodcategory, name="add_foodcategory"),
    path('edit_foodcategory/<int:id>/', views.edit_foodcategory, name="edit_foodcategory"),
    path('update_foodcategory/<int:id>/', views.update_foodcategory, name="update_foodcategory"),
    path('view_foodcategory/', views.view_foodcategory, name="view_foodcategory"),
    path('delete_foodcategory/<int:id>/', views.delete_foodcategory, name="delete_foodcategory"),

    path('agency_order_details/<int:id>/', views.agency_order_details, name="agency_order_details"),
    path('agency_orders/', views.agency_orders, name="agency_orders"),
    path('agency_change_password/', views.agency_change_password, name="agency_change_password"),
    path('agency_profile/', views.agency_profile, name="agency_profile"),

    
]
