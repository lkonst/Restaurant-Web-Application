from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),
    path("bookings", views.bookings, name="bookings"),
    path("menu/items/", views.MenuItemView.as_view(), name="menu_items"),
    path("menu/items/<int:pk>/", views.SingleMenuItemView.as_view(), name="single_menu_item"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
