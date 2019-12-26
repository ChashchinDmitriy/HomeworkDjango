from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Review, Room
from ..serializers import ReviewSerializer


class GetAllReviewsTest(TestCase):
    def setUp(self):
        Room.objects.create(title='Стандартный двуместный номер (две кровати)',
                            description='Двуместный номер с двумя односпальными кроватями и базовым набором удобств: зеркало, шкаф для одежды, тумбочка для личных вещей.',
                            price=1500)
        Room.objects.create(title='Одноместный номер с собственной ванной',
                            description='Одноместный номер с дополнительными удобствами - отдельной ванной комнатой.',
                            price=1750)
        Review.objects.create(room_id=1,
                              name="Дмитрий",
                              arrival_date="2019-12-01",
                              departure_date="2019-12-05",
                              review_text="Остановился на 4 ночи в данном номере. Остался очень доволен. Чистый уютный номер, отзывчивый персонал, топ за свои деньги так сказатб")
        Review.objects.create(room_id=2,
                              name="Мария",
                              arrival_date="2019-11-01",
                              departure_date="2019-12-01",
                              review_text="Приехала в командировку, выбор компании пал на данный номер. После проживания в нем в течение целого месяца с уверенностью могу сказать - Это. Просто. Ахуенно")
        Review.objects.create(room_id=2,
                              name="Dmitriy Chashchin",
                              arrival_date="2019-01-01",
                              departure_date="2019-12-05",
                              review_text="123")

    def test_get_all_reviews(self):
        response = client.get(reverse('review-list'))
        reviews = Review.objects.all()
        print(reviews.count())
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
