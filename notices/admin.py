from django.contrib import admin
from . models import Notice

# Register your models here.
class NoticeModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "title", "content","image","image1", "timestamp", "updated"]
	list_display_links  = ["user", "updated", "timestamp"]
	list_editable		= ["image", "image1", "title"]
	list_filter			= ["user", "title", "timestamp"]
	search_fields		= ["user", "title","content"]
	class Meta:
		model = Notice

admin.site.register(Notice, NoticeModelAdmin)