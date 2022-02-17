import imp
from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth.models import User
from booking.models import Reservation

class AccountView(View):

	def get(self, request):
		if request.user.is_authenticated:
			user = User.objects.get(id=request.user.id)
			reservations = Reservation.objects.filter(user=user.id)
			context = {
				'user': user,
				'reservations': reservations
			}
			return render(request, "account/reservations.html", context)
		else:
			return redirect(f"/accounts/google/login/?next=%2Faccount")
