from django.contrib import admin
from . models import FoodOrder

# Register your models here.
class FoodOrderModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "status", "meal", "location","amount", "refrence", "lat","lng", "timestamp", "updated"]
	list_display_links  = ["user", "meal", "timestamp"]
	list_editable		= ["status"]
	list_filter			= ["user", "meal", "timestamp", "updated"]
	search_fields		= ["meal", "location"]
	class Meta:
		model = FoodOrder


admin.site.register(FoodOrder, FoodOrderModelAdmin)
