from django.db import models


# Create your models here.
class Student(models.Model):
	regnumber  	= models.CharField(max_length=500, unique=True)
	password    = models.CharField(max_length=100)
	first_name  = models.CharField(max_length=500, null=True, blank=True)
	last_name   = models.CharField(max_length=500, null=True, blank=True)
	email       = models.CharField(max_length=500, unique=True)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.regnumber

	class Meta:
		ordering = ["-timestamp", "-updated"]