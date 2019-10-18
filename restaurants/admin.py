from django.contrib import admin
from . models import Restaurant, Meal

# Register your models here.
class RestaurantModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "location","lat","lng", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["name", "location", "lat", "lng"]
	list_filter			= ["user", "timestamp", "updated"]
	search_fields		= ["name", "location"]
	class Meta:
		model = Restaurant


class MealModelAdmin(admin.ModelAdmin):
	list_display 		= ["restaurant", "name", "price", "timestamp", "updated"]
	list_display_links  = ["restaurant", "price", "updated", "timestamp"]
	list_editable		= ["name"]
	list_filter			= ["restaurant", "name"]
	search_fields		= ["restaurant", "name", "price"]
	class Meta:
		model = Meal

admin.site.register(Restaurant, RestaurantModelAdmin)
admin.site.register(Meal, MealModelAdmin)