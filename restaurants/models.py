from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
	user      = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	name      = models.CharField(max_length=500)
	location  = models.CharField(max_length=200)
	lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name + ' - ' + self.location

	class Meta:
		ordering = ["-timestamp", "-updated"]


class Meal(models.Model):
	restaurant  = models.ForeignKey(Restaurant, default=1, on_delete = models.CASCADE)
	name        = models.CharField(max_length=500)
	price       = models.DecimalField(max_digits=6, decimal_places=2)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["timestamp", "updated"]