from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Meal


class FoodOrder(models.Model):
	user      = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	status    = models.CharField(max_length=200, default='pending')
	meal      = models.ForeignKey(Meal, default=1, on_delete = models.CASCADE)
	amount    = models.DecimalField(max_digits=6, decimal_places=2)
	location  = models.CharField(max_length=200)
	lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	refrence  = models.CharField(max_length=200)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.refrence + ' - ' + self.location

	class Meta:
		ordering = ["-timestamp", "-updated"]
