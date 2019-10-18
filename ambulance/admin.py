from django.contrib import admin
from . models import AmbulanceRequests

# Register your models here.
class AmbulanceRequestsModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "status", "problem", "location", "lat", "lng", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["status"]
	list_filter			= ["user", "timestamp"]
	search_fields		= ["user", "problem", "location"]
	class Meta:
		model = AmbulanceRequests

admin.site.register(AmbulanceRequests, AmbulanceRequestsModelAdmin)