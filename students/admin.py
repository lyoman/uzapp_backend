from django.contrib import admin
from . models import Student

class StudentModelAdmin(admin.ModelAdmin):
	list_display 		= ["regnumber", "first_name", "last_name","password",  "email","timestamp"]
	list_display_links  = ["regnumber", "timestamp"]
	list_editable		= ["first_name", "last_name", "email"]
	list_filter			= ["regnumber", "timestamp"]
	search_fields		= ["regnumber", "first_name", "last_name", "email"]
	class Meta:
		model = Student


admin.site.register(Student, StudentModelAdmin)