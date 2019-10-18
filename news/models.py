from django.db import models
from django.contrib.auth.models import User


News_Readers= (
    ('students',   'students only'),
    ('staff',   'staff only'),
    ('everyone', 'everyone'),
    )

# Create your models here.
class Reader(models.Model):
    name      = models.CharField(max_length=200, default='everyone',  choices= News_Readers)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]

class New(models.Model):
	user      = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	reader    = models.ForeignKey(Reader, default=1, on_delete = models.CASCADE)
	title     = models.CharField(max_length=200)
	content   = models.CharField(max_length=600)
	image     = models.ImageField(upload_to = 'news/', blank=True)
	link_url  = models.CharField(max_length=200, blank=True)
	news_date = models.DateField(auto_now=False, auto_now_add=True)
	news_time = models.TimeField(auto_now=False, auto_now_add=True)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]