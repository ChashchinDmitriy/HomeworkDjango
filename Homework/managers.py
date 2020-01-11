from django.db.models import Manager, QuerySet

class RoomQuerySet(QuerySet):
    def room_set(self):
        return self.all()

class RoomManager(Manager):
    def get_queryset(self):
        return RoomQuerySet(self.model, using=self._db)

class RoomPremiumManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_premium=True)