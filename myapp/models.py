from django.db import models


class Room(models.Model):
    room_id = models.CharField(max_length=10, unique=True)
    room_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
