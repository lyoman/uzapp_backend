from django.contrib import admin
from . models import Janitor, Commitie, RezHall, Warden


class CommitieModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "role","name", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp", "role"]
	list_editable		= ["user"]
	list_filter			= ["role", "timestamp"]
	search_fields		= ["user", "role", "name"]
	class Meta:
		model = Commitie


class JanitorModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp", "name"]
	list_editable		= ["user"]
	list_filter			= ["name", "timestamp"]
	search_fields		= ["user", "name"]
	class Meta:
		model = Janitor


class RezHallModelAdmin(admin.ModelAdmin):
	list_display 		= ["name", "capacity", "location", "lat", "lng", "janitor","commitie", "warden", "timestamp", "updated"]
	list_display_links  = ["capacity", "updated", "timestamp"]
	list_editable		= ["warden", "janitor", "commitie","location", "lat", "lng"]
	list_filter			= ["capacity","timestamp", "updated"]
	search_fields		= ["location", "name", "janitor", "warden"]
	class Meta:
		model = RezHall

class WardenModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp", "name"]
	list_editable		= ["user"]
	list_filter			= ["name", "timestamp"]
	search_fields		= ["user", "name"]
	class Meta:
		model = Warden



admin.site.register(Commitie, CommitieModelAdmin)
admin.site.register(Janitor, JanitorModelAdmin)
admin.site.register(RezHall, RezHallModelAdmin)
admin.site.register(Warden, WardenModelAdmin)