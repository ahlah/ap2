from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User

from .models import Hotel, Reservation, Review
from .forms import ReservationForm, ReviewForm

class HotelView(View):

    def get(self, request, id):
        hotel = Hotel.objects.get(id=id)
        reviews = Review.objects.filter(hotel=hotel).order_by("-rating")
        context = {
            'hotel': hotel,
            'reviews': reviews
        }
        return render(request, 'booking/hotel.html', context)

class ReservationView(View):

    def post(self, request, id):
        hotel = Hotel.objects.get(id=id)
        form = ReservationForm(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                adults = form.cleaned_data['adults']
                children = form.cleaned_data['children']
                checkin = form.cleaned_data['checkin']
                checkout = form.cleaned_data['checkout']
        
                reservation = Reservation(user=request.user, hotel=hotel, adults=adults, children=children, checkin=checkin, checkout=checkout )
                reservation.save()
            return redirect(f"/booking/hotel/{id}")
        else:
            return redirect(f"/accounts/google/login/?next=%2Fbooking%2Fhotel%2F{id}")

class ReviewView(View):

    def post(self, request, id):
        hotel = Hotel.objects.get(id=id)
        form = ReviewForm(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                title = form.cleaned_data['title']
                rating = form.cleaned_data['rating']
                description = form.cleaned_data['description']

                ratings = len(Review.objects.filter(hotel=hotel))
                Hotel.objects.filter(id=hotel.id).update(rating=(((ratings * hotel.rating) + rating)/(ratings + 1)))

                review = Review(user=request.user, hotel=hotel, title=title, rating=rating, description=description)
                review.save()

            return redirect(f"/booking/hotel/{id}")
        else:
            return redirect(f"/accounts/google/login/?next=%2Fbooking%2Fhotel%2F{id}")            

