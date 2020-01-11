from rest_framework import serializers

from .models import Review, Room


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('room', 'name', 'arrival_date', 'departure_date', 'review_text')


class RoomListSerializer(serializers.ModelSerializer):
    preview_text = serializers.SerializerMethodField()

    def get_preview_text(self, room):
        return room.get_text_preview()

    class Meta:
        model = Room
        fields = ('title', 'description', 'price', 'preview_text')


class RoomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()


class RoomDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('title', 'description', 'price', 'reviews')
