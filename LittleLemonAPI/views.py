from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class MenuItemView(ListCreateAPIView):
    """GET list, POST create"""

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemDetailView(RetrieveUpdateDestroyAPIView):
    """GET one, PUT/PATCH update, DELETE"""

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
