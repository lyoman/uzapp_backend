from django.db import models
from django.contrib.auth.models import User

Name= (
    ('club',   'clubs'),
    ('sport',   'sports'),
    )

class Category(models.Model):
	name      = models.CharField(max_length=200, choices= Name, unique=True)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp", "-updated"]

class Facility(models.Model):
	name      = models.CharField(max_length=200)
	capacity  = models.CharField(max_length=200)
	specification  = models.CharField(max_length=200)
	location  = models.CharField(max_length=200, unique=True)
	lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name + ' - ' + self.capacity

	class Meta:
		ordering = ["-timestamp", "-updated"]


class SportsandClub(models.Model):
	category  = models.ForeignKey(Category, default=1, on_delete = models.CASCADE)
	facility  = models.ForeignKey(Facility, default=1, on_delete = models.CASCADE)
	coach     = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	captain   = models.CharField(max_length=200)
	name      = models.CharField(max_length=200)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp", "-updated"]

class Event(models.Model):
	title       = models.CharField(max_length=500)
	venue       = models.ForeignKey(Facility, default=1, on_delete = models.CASCADE, blank=True, null=True)
	custom_venue = models.CharField(max_length=200, blank=True, null=True)
	description = models.CharField(max_length=500)
	link_url    = models.CharField(max_length=200, blank=True, null=True)
	event_date  = models.DateField(auto_now=False, auto_now_add=True)
	event_time  = models.TimeField(auto_now=False, auto_now_add=True)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]