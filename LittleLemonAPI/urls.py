from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, msg

urlpatterns = [
    path("menu-items/", MenuItemsView.as_view(), name="menu-item-list"),
    path("menu-items/<int:pk>/", SingleMenuItemView.as_view(), name="menu-item-detail"),
    path("message/", msg),
]
