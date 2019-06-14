from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.city_office)
admin.site.register(models.city_office_staff)
admin.site.register(models.health_center)
admin.site.register(models.health_center_staff)
admin.site.register(models.inventory)
admin.site.register(models.orders)