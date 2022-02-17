from django.urls import path

from .views import HotelView, ReservationView, ReviewView

urlpatterns = [
    path('hotel/<int:id>/', HotelView.as_view()),
    path('hotel/<int:id>/reservation', ReservationView.as_view()),
    path('hotel/<int:id>/review', ReviewView.as_view()),
]
