from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from search.models import Hotel

class Reservation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	adults = models.DecimalField(max_digits=2, decimal_places= 0)
	children = models.DecimalField(max_digits=2, decimal_places=0)
	checkin = models.DateField(auto_now= False, auto_now_add= False)
	checkout = models.DateField(auto_now= False, auto_now_add= False)

	def __str__(self):
		return f"{self.user.username} {self.hotel.title}"

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)
	title = models.CharField(max_length=120)
	description = models.TextField()
	rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, validators=[MinValueValidator(0.5), MaxValueValidator(5.0)])

	def __str__(self):
		return f"{self.user.username} {self.hotel.title}"
