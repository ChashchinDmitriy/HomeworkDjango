from django.shortcuts import (get_object_or_404,
                              redirect, render,
                              render_to_response)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import ReviewForm, QuestionForm, BookingForm
from .models import Room, Review
from .serializers import (ReviewSerializer, RoomCreateUpdateSerializer, RoomDetailSerializer, RoomListSerializer)


def main(request):
    reviews = Review.objects.all()
    return render(request, 'main.html', {'reviews': reviews})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'Room_list.html', {'rooms': rooms})

def room_detail(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        form1 = BookingForm(request.POST)
        if form1.is_valid():
            booking = form1.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('room_detail', id=room.id)
    else:
        form1 = BookingForm()
    if request.method == "POST":
        form2 = ReviewForm(request.POST)
        if form2.is_valid():
            review = form2.save(commit=False)
            review.room = room
            review.save()
            return redirect('room_detail', id=room.id)
    else:
        form2 = ReviewForm()
    return render(request, 'Room.html', {'room': room, 'form1': form1, 'form2': form2})

def add_review(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.room = room
            review.save()
            return redirect('room_detail', id=room.id)
    else:
        form = ReviewForm()
    return render(request, 'Add_review.html', {'form': form})

def contacts(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('contacts')
    else:
        form = QuestionForm()
    return render(request, 'contacts.html', {'form': form})

def booking(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('room_detail', id=room.id)
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


class ActionSerializedViewSet(viewsets.ModelViewSet):
    action_serializers = {}

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return self.serializer_class

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class RoomsViewSet(ActionSerializedViewSet):
    serializer_class = RoomListSerializer
    queryset = Room.objects.all()

    action_serializers = {
        'list': RoomListSerializer,
        'retrieve': RoomDetailSerializer,
        'create': RoomCreateUpdateSerializer,
        'update': RoomCreateUpdateSerializer,
    }

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    @action(detail=False)
    def premium_rooms(self, request):
        premium_rooms = Room.premium.all()

        serializer = self.get_serializer(premium_rooms, many=True)
        return Response(serializer.data)

    @action(detail=True,
            methods=['post'])
    def get_premium(self, request, pk=None):
        room = self.get_object()
        room.publish()
        return Response({'message': 'room got premium'}, status=status.HTTP_200_OK)
