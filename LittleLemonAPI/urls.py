from django.urls import path
from .views import MenuItemView, SingleMenuItemView, msg

urlpatterns = [
    path("menu-items/", MenuItemView.as_view(), name="menu-item-list"),
    path("menu-items/<int:pk>/", SingleMenuItemView.as_view(), name="menu-item-detail"),
    path('message/', msg),
]
