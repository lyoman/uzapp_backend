from django.contrib import admin
from . models import New, Reader

class NewsModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "reader", "title", "content","image", "link_url", "news_date", "news_time", "timestamp", "updated"]
	list_display_links  = ["user", "reader", "updated", "timestamp"]
	list_editable		= ["title","content", "image", "link_url"]
	list_filter			= ["reader", "news_date", "user"]
	search_fields		= ["title", "content", "reader"]
	class Meta:
		model = New

class ReaderModelAdmin(admin.ModelAdmin):
	list_display 		= ["name", "timestamp", "updated"]
	list_display_links  = ["name", "updated", "timestamp"]
	# list_editable		= ["name"]
	list_filter			= ["name"]
	search_fields		= ["name"]
	class Meta:
		model = Reader


admin.site.register(New, NewsModelAdmin)
admin.site.register(Reader, ReaderModelAdmin)

