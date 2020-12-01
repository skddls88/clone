from django.urls import path
from room import views as room_views

add_name = "core"

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]