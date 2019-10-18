from django.db import models
from django.contrib.auth.models import User

class AmbulanceRequests(models.Model):
	user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	status      = models.CharField(max_length=200, default='pending')
	location    = models.CharField(max_length=300)
	lat         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	lng         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	problem     = models.CharField(max_length=500)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.location + ' - ' + self.status

	class Meta:
		ordering = ["-timestamp", "-updated"]