from django.contrib import admin

# Register your models here.
from . models import Rule

class RulesModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "category", "details", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["name","category", "details"]
	list_filter			= ["name", "category", "user"]
	search_fields		= ["name", "category", "details"]
	class Meta:
		model = Rule


admin.site.register(Rule, RulesModelAdmin)
 