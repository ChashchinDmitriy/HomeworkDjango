from django.test import TestCase

from ..models import Room


class RoomTest(TestCase):
    def setUp(self):
        Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                            description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                            price=1000)
        Room.objects.create(title='Одноместный номер с собственной ванной',
                            description='Одноместный номер с дополнительными удобствами - отдельной ванной комнатой.',
                            price=1500)
        Room.objects.create(title='Королевский двуместный номер',
                            description='Наилучший из доступных в нашем отеле номеров. Наслаждайтесь двуспальной кроватью типа queen-size, личной ванной комнатой с большой душевой кабиной и ванной, кондиционером. В цену включены завтрак и утренний массаж!',
                            price=4000)

    def test_premium_and_filtering(self):
        room = Room.objects.get(title='Королевский двуместный номер')
        room.get_premium()
        self.assertEqual(room.is_premium, True)
        rooms = Room.premium.all()
        self.assertEqual(rooms.count(), 1)
