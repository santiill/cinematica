from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from booking.models import Room
from cinema.models import Movie, Cinema, Showtime

from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "name",
            "description",
            "picture",
            "release_date",
            "rental_over_date",
        ]


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            "id",
            "name",
            "description",
            "address",
            "contacts",
            "open_from",
            "closed_from",
        ]


class RoomSerializer(WritableNestedModelSerializer):
    cinema = PresentablePrimaryKeyRelatedField(
        queryset=Cinema.objects.all(), presentation_serializer=CinemaSerializer
    )

    class Meta:
        model = Room
        fields = ["id", "name", "cinema"]


class ShowtimeSerializer(WritableNestedModelSerializer):
    room = PresentablePrimaryKeyRelatedField(
        queryset=Room.objects.all(), presentation_serializer=RoomSerializer
    )
    movie = PresentablePrimaryKeyRelatedField(
        queryset=Movie.objects.all(), presentation_serializer=MovieSerializer
    )

    class Meta:
        model = Showtime
        fields = ["id", "room", "movie", "start_time", "end_time"]