from rest_framework import serializers
from . import models

class city_office_serializer(serializer.ModelSerializer):
	class Meta:
		model = models.city_office
		fields = ('city_office_id', 'city_office_name')

class city_office_staff_serializer(serializer.ModelSerializer):
	class Meta:
		model - models.city_office_staff
		fields = ('city_office_staff_id', 'city_office_id', 'city_office_staff_name')

class health_center_serializer(serializer.ModelSerializer):
	class Meta:
		model = models.health_center
		fields = ('health_center_id', 'city_office_id', 'health_center_name', 'health_center_location')

class health_center_staff_serializer(serializer.ModelSerializer):
	class Meta:
		model = models.health_center_staff
		fields = ('health_center_staff_id', 'health_center_id', 'health_center_staff_name')

class inventory_serializer(serializer.ModelSerializer):
	class Meta:
		model = models.inventory
		fields = ('product_code', 'health_center_id', 'product_name', 'current_quantity', 'starting_quantity')

class orders_serializer(serializer.ModelSerializer):
	class Meta:
		model = models.orders
		fields = ('order_id', 'health_center_id', 'city_office_id', 'product_code', 'order_quantity', 'order_status')