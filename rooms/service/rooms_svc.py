from rooms.models import Room


def list_all_rooms():
    return [room.to_dict_json() for room in Room.objects.all()]
