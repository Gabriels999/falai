from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rooms.service import rooms_svc

# Create your views here.


@login_required
def rooms_list(request):
    return render(
        request,
        'rooms/rooms_list.html',
        {'rooms': rooms_svc.list_all_rooms()})


@login_required
def detailed_room(request, slug):
    return render(
        request,
        'rooms/detailed_room.html',
        {
            'room': rooms_svc.get_room(slug),
            'messages': rooms_svc.get_messages(slug)[0:25]
        })
