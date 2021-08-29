from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Categories

# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()