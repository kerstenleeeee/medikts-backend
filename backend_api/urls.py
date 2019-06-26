from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend_api import views

urlpatterns = [
  path('city_office/offices/all', views.city_office_list),
  path('city_office/staff/all', views.city_office_staff_list),
  path('health_center/centers/all', views.health_center_list),
  path('health_center/staff/all', views.health_center_staff_list),
  path('inventory/all', views.inventory_list),
  path('orders/all', views.orders_list),
  path('city_office/offices/detail/<int:pk>/', views.city_office_object),
  path('city_office/staff/detail/<int:pk>/', views.city_office_staff_object),
  path('health_center/centers/detail/<int:pk>/', views.health_center_object),
  path('health_center/staff/detail/<int:pk>/', views.health_center_staff_object),
  path('inventory/detail/<int:pk>/', views.inventory_object),
  path('orders/detail/<int:pk>/', views.orders_object),
  path('login/', views.login)
]

urlpatterns = format_suffix_patterns(urlpatterns)