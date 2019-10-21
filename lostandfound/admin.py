from django.contrib import admin
from . models import Lost

# Register your models here.
class LostModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "place","image", "contact", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["image", "contact", "place", "name"]
	list_filter			= ["user", "name", "timestamp"]
	search_fields		= ["user", "name","contact"]
	class Meta:
		model = Lost

admin.site.register(Lost, LostModelAdmin)
