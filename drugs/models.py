from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drug(models.Model):
	user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	name        = models.CharField(max_length=200)
	status    	= models.CharField(max_length=200, default='available')
	price       = models.CharField(max_length=200, blank=True)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp", "-updated"]