from django.test import TestCase, Client
import json
from .models import Room


class RoomAPITest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_room(self):
        # 測試成功創建房間
        data = {'room_id': 'R001', 'room_name': '測試房間', 'user_name': '測試用戶'}
        response = self.client.post('/rooms/create/',
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Room.objects.filter(room_id='R001').exists())

    def test_create_room_invalid_method(self):
        # 測試使用錯誤的 HTTP 方法
        response = self.client.get('/rooms/create/')
        self.assertEqual(response.status_code, 405)
