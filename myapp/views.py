from django.shortcuts import render, HttpResponse
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
