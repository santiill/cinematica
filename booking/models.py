from django.db import models
from django.conf import settings

from cinema.models import Room, Showtime


class Seat(models.Model):
    seat_number = models.PositiveIntegerField()
    row = models.PositiveIntegerField()
    room = models.ForeignKey(
        Room, related_name="seats", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.seat_number}'


class Discount(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    discount_card = models.DecimalField(
        max_digits=9, decimal_places=2, default=0
    )

    def __str__(self):
        return f"{self.client} discount card"


class TicketType(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0, null=True, blank=True
    )

    def __str__(self):
        return f'{self.name}'


class Booking(models.Model):
    CARD = "card"
    MOBILE = "mobile"
    E_WALlET = "e-Wallet"

    PaymentOptions = ((CARD, CARD), (MOBILE, MOBILE), (E_WALlET, E_WALlET))

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, null=True, blank=True
    )
    payment_method = models.CharField(max_length=255, choices=PaymentOptions)
    payment_value = models.CharField(max_length=200)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.client is not None:
            return (
                str(self.client)
                + "'s ticket for showtime "
                + str(self.showtime)
                + " seat number "
                + str(self.seat)
            )
        else:
            return (
                "Anonymous ticket for "
                + str(self.showtime)
                + " seat number "
                + str(self.seat)
            )

    def save(self, *args, **kwargs):
        if (
            self.ticket_type.name == "ADULT"
            or self.ticket_type.name == "CHILD"
        ):
            if self.discount is None:
                self.price = self.ticket_type.price
            else:
                price_with_discount = (
                    self.ticket_type.price / 100 * self.discount.discount_card
                )
                self.price = self.ticket_type.price - price_with_discount
        super().save(*args, **kwargs)