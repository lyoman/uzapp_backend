from django.contrib import admin
from . models import LaptopsRegister

# Register your models here.
class LaptopsRegisterModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "model", "color","serialnumber","barcode","ownership", "macaddress", "make", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["serialnumber", "model"]
	list_filter			= ["user", "color", "timestamp"]
	search_fields		= ["user", "color","barcode", "ownership", "model", "serialnumber"]
	class Meta:
		model = LaptopsRegister

admin.site.register(LaptopsRegister, LaptopsRegisterModelAdmin)