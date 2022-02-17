from django.db import models

class Hotel(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	city = models.CharField(max_length=75, default="")
	country = models.CharField(max_length=75, default="")
	price = models.DecimalField(max_digits=100, decimal_places= 2)
	rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
	img1 = models.ImageField(default='default.jpg')
	img2 = models.ImageField(default='default.jpg')
	img3 = models.ImageField(default='default.jpg')
	img4 = models.ImageField(default='default.jpg')
	img5 = models.ImageField(default='default.jpg')

	def __str__(self):
		return f"{self.title}"
	
