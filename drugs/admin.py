from django.contrib import admin

# Register your models here.
from . models import Drug

class DrugsModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "price", "status", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["name","status", "price"]
	list_filter			= ["name", "price", "user"]
	search_fields		= ["name", "status", "price"]
	class Meta:
		model = Drug


admin.site.register(Drug, DrugsModelAdmin)
