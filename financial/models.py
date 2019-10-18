from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FinancialStatement(models.Model):
	user        = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
	date  	    = models.DateField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length=100)
	debit       =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	credit      =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	closing_balance =  models.DecimalField(max_digits=6, decimal_places=2)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ["timestamp", "-updated"]