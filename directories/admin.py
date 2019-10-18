from django.contrib import admin
from . models import Department, Faculty, PhoneNumber


class FacultyModelAdmin(admin.ModelAdmin):
	list_display 		= ["shortname", "fullname","location", "lat", "lng", "dean", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp", "shortname"]
	list_editable		= ["fullname", "location", "dean", "lat", "lng"]
	list_filter			= ["shortname", "timestamp"]
	search_fields		= ["fullname", "shortname", "location"]
	class Meta:
		model = Faculty


class DepartmentModelAdmin(admin.ModelAdmin):
	list_display 		= ["faculty", "shortname", "fullname","location","chairman", "email", "lat", "lng", "timestamp", "updated"]
	list_display_links  = ["updated", "timestamp", "shortname"]
	list_editable		= ["fullname", "email", "chairman","lat", "lng"]
	list_filter			= ["shortname","faculty", "timestamp"]
	search_fields		= ["fullname", "shortname"]
	class Meta:
		model = Department


class PhoneNumberModelAdmin(admin.ModelAdmin):
	list_display 		= ["department", "phone", "timestamp", "updated"]
	list_display_links  = ["department", "updated", "timestamp"]
	list_editable		= ["phone"]
	list_filter			= ["department","timestamp", "updated"]
	search_fields		= ["phone", "department"]
	class Meta:
		model = PhoneNumber



admin.site.register(Faculty, FacultyModelAdmin)
admin.site.register(Department, DepartmentModelAdmin)
admin.site.register(PhoneNumber, PhoneNumberModelAdmin)