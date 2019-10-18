from django.db import models
from django.contrib.auth.models import  User
from django.core.validators import RegexValidator

# Create your models here.
class Faculty(models.Model):
    shortname = models.CharField(max_length=200)
    fullname  = models.CharField(max_length=200)
    location  = models.CharField(max_length=200)
    lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    dean      = models.CharField(max_length=200)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.fullname + ' - ' + self.shortname

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Department(models.Model):
	faculty   = models.ForeignKey(Faculty, default=1, on_delete = models.CASCADE)
	shortname = models.CharField(max_length=200)
	fullname  = models.CharField(max_length=200)
	location  = models.CharField(max_length=200)
	lat       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	chairman  = models.CharField(max_length=200)
	email     = models.CharField(max_length=200)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.fullname + ' - ' + self.shortname

	class Meta:
		ordering = ["-timestamp", "-updated"]

class PhoneNumber(models.Model):
	department  = models.ForeignKey(Department, default=1, on_delete = models.CASCADE)
	# phone       = models.CharField(max_length=500)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone       = models.CharField(validators=[phone_regex], max_length=17, blank=False, unique=True) # validators should be a list
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.phone

	class Meta:
		ordering = ["-timestamp", "-updated"]