from django.contrib import admin
from . models import LaptopsRegister

# Register your models here.
class LaptopsRegisterModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "laptopname", "color","serialnumber", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["serialnumber", "laptopname"]
	list_filter			= ["user", "color", "timestamp"]
	search_fields		= ["user", "color", "laptopname", "serialnumber"]
	class Meta:
		model = LaptopsRegister

admin.site.register(LaptopsRegister, LaptopsRegisterModelAdmin)