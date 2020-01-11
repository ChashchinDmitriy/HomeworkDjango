import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Room
from ..serializers import RoomListSerializer, RoomDetailSerializer

client = Client()


class GetAllRoomsTest(TestCase):
    def setUp(self):
        Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                            description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                            price=1500)
        Room.objects.create(title='Одноместный номер с собственной ванной',
                            description='Одноместный номер с дополнительными удобствами - отдельной ванной комнатой.',
                            price=1750)

    def test_get_all_rooms(self):
        response = client.get(reverse('room-list'))
        rooms = Room.objects.all()
        serializer = RoomListSerializer(rooms, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleReviewTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                                        description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                                        price=1500)

    def test_get_valid_single_room(self):
        response = client.get(reverse('room-detail', kwargs={'pk': self.room.pk}))
        room = Room.objects.get(pk=self.room.pk)
        serializer = RoomDetailSerializer(room)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_room(self):
        response = client.get(reverse('room-detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRoomTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'title': 'Стандартный двуместный номер (две кровати)',
            'description': 'Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
            'price': 1500,
        }
        self.invalid_payload = {
            'title': 'Стандартный двуместный номер (две кровати)',
            'description': 'Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
        }

    def test_create_valid_single_room(self):
        response = client.post(reverse('room-list'),
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_room(self):
        response = client.post(reverse('room-list'),
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleRoomTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                                        description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                                        price=1500)
        self.valid_payload = {
            'title': 'Стандартный двуместный номер (две кровати)',
            'description': 'New',
            'price': 1500,
        }
        self.invalid_payload = {
            'title': 'Стандартный двуместный номер (две кровати)',
            'description': None,
            'price': 1500,
        }

    def test_valid_update_room(self):
        response = client.put(reverse('room-detail',
                                      kwargs={'pk': self.room.pk}),
                              data=json.dumps(self.valid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_room(self):
        response = client.put(reverse('room-detail',
                                      kwargs={'pk': self.room.pk}),
                              data=json.dumps(self.invalid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePostTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                                        description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                                        price=1500)

    def test_valid_delete_room(self):
        response = client.delete(
            reverse('room-detail', kwargs={'pk': self.room.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_room(self):
        response = client.delete(reverse('room-detail', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
