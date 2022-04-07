from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from cinema.models import Movie, Cinema, Showtime, Room
from cinema.serializers import (
    MovieSerializer,
    CinemaSerializer,
    ShowtimeSerializer, RoomSerializer,
)
from users.permissions import IsAdminOrReadOnly


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(
        release_date__lte=datetime.now(),
        rental_over_date__gt=datetime.now()
    )
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaList(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ShowtimeList(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["room__cinema", "movie", "start_time", "end_time"]


class ShowtimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminOrReadOnly,)