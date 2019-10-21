from django.contrib import admin
from . models import Home

# Register your models here.
class HomeModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "title", "content","banner","banner1","banner2", "banner3", "link_url", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["banner", "banner1", "banner2", "banner3"]
	list_filter			= ["user", "title", "timestamp"]
	search_fields		= ["user", "title","content"]
	class Meta:
		model = Home

admin.site.register(Home, HomeModelAdmin)