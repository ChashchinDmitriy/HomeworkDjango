from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('room', 'name', 'arrival_date', 'departure_date', 'review_text')


'''
class BookingListSerializer(serializers.ModelSerializer):
    preview_text = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ('title', 'author', 'created_date', 'preview_text')

class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()'''
