from django.contrib import admin
from . models import Category, Facility, Event, SportsandClub


class FacilityModelAdmin(admin.ModelAdmin):
	list_display 		= ["name", "capacity","specification","location", "lat", "lng", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp", "location"]
	list_editable		= ["capacity"]
	list_filter			= ["location", "timestamp"]
	search_fields		= ["location", "capacity", "name"]
	class Meta:
		model = Facility


class CategoryModelAdmin(admin.ModelAdmin):
	list_display 		= ["name", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp"]
	list_editable		= ["name"]
	list_filter			= ["timestamp"]
	search_fields		= ["name"]
	class Meta:
		model = Category


class EventModelAdmin(admin.ModelAdmin):
	list_display 		= ["title", "venue", "custom_venue", "description", "link_url", "event_date","event_time", "timestamp", "updated"]
	list_display_links  = ["venue", "updated", "timestamp"]
	list_editable		= ["description"]
	list_filter			= ["title","timestamp", "updated"]
	search_fields		= ["title", "venue", "description", "link_url"]
	class Meta:
		model = Event

class SportsandClubModelAdmin(admin.ModelAdmin):
	list_display 		= ["category", "facility","coach", "captain", "name", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp"]
	list_editable		= ["coach", "captain"]
	list_filter			= ["name", "timestamp"]
	search_fields		= ["name", "coach", "captain", "facility"]
	class Meta:
		model = SportsandClub



admin.site.register(Facility, FacilityModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(SportsandClub, SportsandClubModelAdmin)