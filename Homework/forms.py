from django import forms

from .models import Booking, Review, Question


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'arrival_date', 'departure_date', 'review_text')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'email', 'question_text')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'arrival_date', 'departure_date', 'phone', 'email')
