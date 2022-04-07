"""root URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from booking.views import *
from cinema.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view()),
    path('', MovieList.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('cinema-list/', CinemaList.as_view(), name='cinema-list'),
    path('cinema/<int:pk>/', CinemaDetail.as_view(), name='cinema-detail'),
    path('showtime-list/', ShowtimeList.as_view(), name='showtime-list'),
    path('showtime/<int:pk>/', ShowtimeDetail.as_view(), name='showtime-detail'),
    path('room-list', RoomList.as_view(), name='room-list'),
    path('seat-list', SeatList.as_view(), name='seat-list'),
    path('booking-list', BookingList.as_view(), name='booking-list'),
    path('discount-list', DiscountList.as_view(), name='discount-list'),
    path('feedback-list', FeedbackList.as_view(), name='feedback-list'),
    path('ticket-type', TicketTypeList.as_view(), name='ticket-type'),
    path('ticket-type/<int:pk>/', TicketTypeDetail.as_view(), name='ticket-detail')
]