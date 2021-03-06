from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class city_office_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.city_office
		fields = ('city_office_id', 'city_office_name')

class city_office_staff_serializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField()

	def get_user(self, obj):
		instance = User.objects.get(pk=obj.user.id)
		return instance.username

	class Meta:
		model = models.city_office_staff
		fields = ('city_office_staff_id', 'city_office_id', 'city_office_staff_name', 'user')

class health_center_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.health_center
		fields = ('health_center_id', 'city_office_id', 'health_center_name', 'health_center_location')

class health_center_staff_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.health_center_staff
		fields = ('health_center_staff_id', 'health_center_id', 'health_center_staff_name', 'user')

class inventory_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.inventory
		fields = ('inventory_id', 'product_code', 'health_center_id', 'product_name', 'current_quantity', 'starting_quantity')

class orders_serializer(serializers.ModelSerializer):
	# product_code = serializers.SerializerMethodField()

	# def get_product_code(self, obj):
	# 	instance = models.inventory.objects.get(inventory_id=obj.product_code)
	# 	return instance.product_name

	# def create(self, validated_data):
	# 	product_code = validated_data.pop('product_code')
	# 	return models.orders.objects.create(**validated_data, product_code=product_code)

	def update(self, instance, validated_data):
		instance.order_status = validated_data.get('order_status', instance.order_status)
		instance.save()
		return instance

	class Meta:
		model = models.orders
		fields = ('order_id', 'health_center_id', 'city_office_id', 'product_code', 'order_quantity', 'order_status')