from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class city_office(models.Model):
	city_office_id = models.AutoField(primary_key = True)
	city_office_name = models.CharField(null = False, blank = False, max_length = 255)

	def __str__(self):
		return '%s (%s)' % (self.city_office_id, self.city_office_name)

class city_office_staff(models.Model):
	city_office_staff_id = models.AutoField(primary_key = True)
	city_office_id  = models.ForeignKey(city_office, related_name = 'staff_city_office_id', on_delete = models.PROTECT)
	city_office_staff_name = models.CharField(null = False, blank = False, max_length = 255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s (%s)' % (self.city_office_staff_id, self.city_office_staff_name, self.city_office_id)

class health_center(models.Model):
	health_center_id = models.AutoField(primary_key = True)
	city_office_id  = models.ForeignKey(city_office, related_name = 'center_city_office_id', on_delete = models.PROTECT)
	health_center_name = models.CharField(null = False, blank = False, max_length = 2555)
	health_center_location = models.CharField(null = False, blank = False, max_length = 255)

	def __str__(self):
		return '%s -> %s' % (self.health_center_id, self.city_office_id)

class health_center_staff(models.Model):
	health_center_staff_id = models.AutoField(primary_key = True)
	health_center_id = models.ForeignKey(health_center, related_name = 'staff_health_center_id', on_delete = models.PROTECT)
	health_center_staff_name = models.CharField(null = False, blank = False, max_length = 255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s (%s)' % (self.health_center_staff_id, self.health_center_staff_name, self.health_center_id)

class inventory(models.Model):
	inventory_id = models.AutoField(primary_key = True, default=0)
	product_code = models.IntegerField()
	health_center_id = models.ForeignKey(health_center, related_name = 'inventory_health_center_id', on_delete = models.PROTECT)
	product_name = models.CharField(null = False, blank = False, max_length = 255)
	current_quantity = models.IntegerField(validators=[MinValueValidator(0)])
	starting_quantity = models.IntegerField(validators=[MinValueValidator(0)])

	def __str__(self):
		return '%s (%s) in %s (%d/%d)' % (self.product_name, self.product_name, self.health_center_id, self.current_quantity, self.starting_quantity)

class orders(models.Model):
	ORDER_STATUS_CHOICES = (
		('Ordered', 'Ordered'),
		('Received', 'Received'),
		('Confirmed', 'Confirmed'),
		('Dispatched', 'Dispatched'),
	)
	order_id = models.AutoField(primary_key = True)
	health_center_id = models.ForeignKey(health_center, related_name = 'order_health_center_id', on_delete = models.PROTECT)
	city_office_id = models.ForeignKey(city_office, related_name = 'order_city_office_id', on_delete = models.PROTECT)
	product_code = models.ForeignKey(inventory, related_name = 'order_product_code', on_delete = models.PROTECT)
	order_quantity = models.IntegerField(validators=[MinValueValidator(0)])
	order_status = models.CharField(max_length = 255, choices = ORDER_STATUS_CHOICES)