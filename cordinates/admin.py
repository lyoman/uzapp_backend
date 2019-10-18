from django.contrib import admin
from . models import Cordinate

class CordinateModelAdmin(admin.ModelAdmin):
	list_display 		= ["name", "location", "icon", "updated", "lat", "lng", "timestamp"]
	list_display_links  = ["location", "timestamp"]
	list_editable		= ["lat", "lng", "name", "icon"]
	list_filter			= ["location", "timestamp"]
	search_fields		= ["name", "location"]
	class Meta:
		model = Cordinate


admin.site.register(Cordinate, CordinateModelAdmin)