from django.db import models
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from django.utils import timezone

from .managers import RoomPremiumManager, RoomManager


class Room(models.Model):
    title = models.CharField(max_length=64, verbose_name="Название комнаты")
    description = models.TextField(verbose_name="Описание комнаты")
    price = models.IntegerField(verbose_name="Цена за ночь")
    is_premium = models.BooleanField(default=False, verbose_name="Лакшери комната?")

    objects = RoomManager()
    premium = RoomPremiumManager()

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if self.price > 1500:
            self.is_premium = True
        super().save(*args, **kwargs)

    def get_text_preview(self):
        return truncatewords(self.description, 25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Question(models.Model):
    name = models.CharField(max_length=64, verbose_name="Ваше имя:")
    email = models.EmailField(max_length=64, verbose_name="Адрес электронной почты")
    question_text = models.TextField(verbose_name="Ваш вопрос:")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Review(models.Model):
    room = models.ForeignKey('Homework.Room',
                             on_delete=models.CASCADE,
                             related_name='reviews')
    name = models.CharField(max_length=64, verbose_name="Ваше имя")
    arrival_date = models.DateField(blank=False,
                                    null=False,
                                    verbose_name="Дата заезда")
    departure_date = models.DateField(blank=False,
                                      null=False,
                                      verbose_name="Дата выезда")
    review_text = models.TextField(verbose_name="Ваш отзыв")
    publish_date = models.DateField(default=timezone.now,
                                    verbose_name="Дата публикации отзыва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Booking(models.Model):
    room = models.ForeignKey('Homework.Room',
                             on_delete=models.CASCADE,
                             related_name='bookings')
    name = models.CharField(max_length=64, verbose_name="Ваше имя")
    arrival_date = models.DateField(blank=False,
                                    null=False,
                                    verbose_name="Дата заезда")
    departure_date = models.DateField(blank=False,
                                      null=False,
                                      verbose_name="Дата выезда")
    phone = models.CharField(max_length=11, verbose_name="Номер телефона")
    email = models.EmailField(max_length=64, verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
