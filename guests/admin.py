from django.contrib import admin
from . models import Guest

class GuestModelAdmin(admin.ModelAdmin):
	list_display 		= ["name", "phone","lat", "lng", "updated", "timestamp"]
	list_display_links  = ["name","phone", "timestamp"]
	# list_editable		= []
	list_filter			= ["phone", "name", "timestamp"]
	search_fields		= ["phone", "name"]
	class Meta:
		model = Guest


admin.site.register(Guest, GuestModelAdmin)