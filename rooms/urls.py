from django.urls import path

from rooms import views

urlpatterns = [
    path('list', views.rooms_list, name="rooms_list"),
    path('<slug:slug>', views.detailed_room, name="detailed_room"),
]
