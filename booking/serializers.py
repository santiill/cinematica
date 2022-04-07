from rest_framework import serializers
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from drf_writable_nested.serializers import WritableNestedModelSerializer

from cinema.models import Room
from cinema.serializers import ShowtimeSerializer, RoomSerializer
from users.serializers import UserSerializer
from .models import Booking, Showtime, Seat, Discount, TicketType


class SeatSerializer(WritableNestedModelSerializer):
    room = PresentablePrimaryKeyRelatedField(
        queryset=Room.objects.all(), presentation_serializer=RoomSerializer
    )

    class Meta:
        model = Seat
        fields = ["id", "seat_number", "row", "room"]


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "client"]
        read_only_fields = ["discount_card"]


class BookingSerializer(WritableNestedModelSerializer):
    seat = PresentablePrimaryKeyRelatedField(
        queryset=Seat.objects.all(),
        presentation_serializer=SeatSerializer)
    client = UserSerializer(read_only=True)
    showtime = PresentablePrimaryKeyRelatedField(
        queryset=Showtime.objects.all(),
        presentation_serializer=ShowtimeSerializer,
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "client",
            "ticket_type",
            "price",
            "discount",
            "payment_method",
            "payment_value",
            "seat",
            "showtime",
            "booking_date",
        ]
        read_only_fields = ["price"]

    def validate(self, attrs):
        seat = attrs.get("seat")
        showtime = attrs.get("showtime")

        if Booking.objects.filter(seat=seat, showtime=showtime).exists():

            raise serializers.ValidationError("Seat is already reserved")
        return attrs