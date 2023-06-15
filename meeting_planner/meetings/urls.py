from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),
    path("rooms", views.rooms_list, name="rooms"),
    path("new_meeting", views.new_meeting, name="new_meeting"),
]
