from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
	user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	title       = models.CharField(max_length=200)
	content    	= models.CharField(max_length=200)
	image       = models.ImageField(upload_to = 'notices/', blank=True)
	image1      = models.ImageField(upload_to = 'notices/', blank=True)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]