from django.db import models

# Create your models here.
class Cordinate(models.Model):
	name       = models.CharField(max_length=50)
	icon       = models.CharField(max_length=50)
	location   = models.CharField(max_length=50)
	lat        = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng        = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	timestamp  = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated    = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name + ' - ' + self.location

	class Meta:
		ordering = ["-timestamp", "-updated"]
