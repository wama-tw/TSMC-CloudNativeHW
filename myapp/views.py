from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Room


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def about(request):
    return HttpResponse("This is the about page.")


def contact(request):
    return HttpResponse("This is the contact page.")


def rooms(request):
    room_items = Room.objects.all()
    room_items_string = [
        f"Room ID: {room.room_id}, Room Name: {room.room_name}, User Name: {room.user_name}\n"
        for room in room_items
    ]
    return HttpResponse(room_items_string)


@csrf_exempt
def create_room(request):
    if request.method != 'POST':
        return JsonResponse({'error': '只接受 POST 請求'}, status=405)

    try:
        data = json.loads(request.body)
        room = Room.objects.create(room_id=data.get('room_id'),
                                   room_name=data.get('room_name'),
                                   user_name=data.get('user_name'))
        return JsonResponse(
            {
                'message': '房間創建成功',
                'room': {
                    'room_id': room.room_id,
                    'room_name': room.room_name,
                    'user_name': room.user_name
                }
            },
            status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': '無效的 JSON 格式'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
