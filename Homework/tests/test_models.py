from django.test import TestCase

from ..models import Room


class RoomTest(TestCase):
    def setUp(self):
        Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                            description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                            price=1500)
        Room.objects.create(title='Одноместный номер с собственной ванной',
                            description='Одноместный номер с дополнительными удобствами - отдельной ванной комнатой.',
                            price=1750)
        Room.objects.create(title='Королевский двуместный номер',
                            description='Наилучший из доступных в нашем отеле номеров. Наслаждайтесь двуспальной кроватью типа queen-size, личной ванной комнатой с большой душевой кабиной и ванной, кондиционером. В цену включены завтрак и утренний массаж!',
                            price=4000)

    def test_rooms_filtering(self):
        rooms = Room.objects.filter(price__gt=1500)
        self.assertEqual(rooms.count(), 2)
