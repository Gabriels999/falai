from django.urls import path

from rooms import views

urlpatterns = [
    path('rooms_list', views.rooms_list, name="rooms_list"),
]
