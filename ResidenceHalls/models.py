from django.db import models
from django.contrib.auth.models import User



class Janitor(models.Model):
	user      = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	name      = models.CharField(max_length=200)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp", "-updated"]


class Warden(models.Model):
	user      = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	name      = models.CharField(max_length=200)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp", "-updated"]

class Commitie(models.Model):
	user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	role        = models.CharField(max_length=500)
	name        = models.CharField(max_length=200)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name + ' - ' + self.role

	class Meta:
		ordering = ["-timestamp", "-updated"]


# Create your models here.
class RezHall(models.Model):
	name      = models.CharField(max_length=200, unique=True)
	capacity  = models.CharField(max_length=200)
	location  = models.CharField(max_length=200, unique=True)
	lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	janitor   = models.ForeignKey(Janitor, default=1, on_delete = models.CASCADE)
	commitie  = models.ForeignKey(Commitie, default=1, on_delete = models.CASCADE)
	warden    = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name + ' - ' + self.location

	class Meta:
		ordering = ["-timestamp", "-updated"]