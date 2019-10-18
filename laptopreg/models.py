from django.db import models
from django.contrib.auth.models import User


class LaptopsRegister(models.Model):
	user          = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	laptopname    = models.CharField(max_length=200)
	color         = models.CharField(max_length=200)
	serialnumber  = models.CharField(max_length=200)
	updated       = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.laptopname + ' - ' + self.serialnumber

	class Meta:
		ordering = ["-timestamp", "-updated"]