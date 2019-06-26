from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

###############################
from . import models
from . import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def city_office_list(request):
    if request.method == 'GET':
        city_office = models.city_office.objects.all()
        serializer = serializers.city_office_serializer(city_office, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.city_office_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def city_office_staff_list(request):
    if request.method == 'GET':
        city_office_staff = models.city_office_staff.objects.all()
        serializer = serializers.city_office_staff_serializer(city_office_staff, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.city_office_staff_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def health_center_list(request):
    if request.method == 'GET':
        health_center = models.health_center.objects.all()
        serializer = serializers.health_center_serializer(health_center, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.health_center_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def health_center_staff_list(request):
    if request.method == 'GET':
        health_center_staff = models.health_center_staff.objects.all()
        serializer = serializers.health_center_staff_serializer(health_center_staff, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.health_center_staff_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def inventory_list(request):
    if request.method == 'GET':
        inventory = models.inventory.objects.all()
        serializer = serializers.inventory_serializer(inventory, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.inventory_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def orders_list(request):
    if request.method == 'GET':
        orders = models.orders.objects.all()
        serializer = serializers.orders_serializer(orders, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.orders_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

############################
############################
############################

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def city_office_object(request, pk):
    try:
        city_office = models.city_office.objects.get(city_office_id = pk)
    except models.city_office.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.city_office_serializer(city_office)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.city_office_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = serializers.city_office_serializer(city_office, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        city_office.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def city_office_staff_object(request, pk):
    try:
        city_office_staff = models.city_office_staff.objects.get(city_office_staff_id = pk)
    except models.city_office_staff.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.city_office_staff_serializer(city_office_staff)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.city_office_staff_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = serializers.city_office_staff_serializer(city_office_staff, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        city_office_staff.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def health_center_object(request, pk):
    try:
        health_center = models.health_center.objects.get(health_center_id = pk)
    except models.health_center.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.health_center_serializer(health_center)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.health_center_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = serializers.health_center_serializer(health_center, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        health_center.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def health_center_staff_object(request, pk):
    try:
        health_center_staff = models.health_center_staff.objects.get(health_center_staff_id = pk)
    except models.health_center_staff.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.health_center_staff_serializer(health_center_staff)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.health_center_staff_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = serializers.health_center_staff_serializer(health_center_staff, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        health_center_staff.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def inventory_object(request, pk):
    try:
        inventory = models.inventory.objects.get(product_code = pk)
    except models.inventory.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.inventory_serializer(inventory)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.inventory_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = serializers.inventory_serializer(inventory, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        inventory.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def orders_object(request, pk):
    try:
        orders = models.orders.objects.get(order_id = pk)
    except models.orders.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.orders_serializer(orders)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.orders_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = serializers.orders_serializer(orders, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        orders.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)