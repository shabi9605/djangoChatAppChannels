from django.urls import path

from . import views


urlpatterns = [
    path("index/", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),

    path("delete_member/<str:room_name>/", views.deleteMember, name="delete_member"),
]