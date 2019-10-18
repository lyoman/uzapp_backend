from django.contrib import admin

# Register your models here.
from . models import Faq

class FaqsModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "name", "question", "answer","link", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["name","question", "answer","link"]
	list_filter			= ["name", "question", "user"]
	search_fields		= ["name", "question", "answer"]
	class Meta:
		model = Faq


admin.site.register(Faq, FaqsModelAdmin)
