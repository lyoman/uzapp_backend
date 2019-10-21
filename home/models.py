from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    user       = models.ForeignKey(User, default=1, on_delete = models.CASCADE)   
    title      = models.CharField(max_length=200)
    content    = models.CharField(max_length=600)
    banner     = models.ImageField(upload_to = 'banner/', blank=True)
    banner1    = models.ImageField(upload_to = 'banner/', blank=True)
    banner2    = models.ImageField(upload_to = 'banner/', blank=True)
    banner3    = models.ImageField(upload_to = 'banner/', blank=True)
    link_url   = models.CharField(max_length=200, blank=True)
    updated    = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.content

    class Meta:
        ordering = ["-timestamp", "-updated"]