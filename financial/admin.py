from django.contrib import admin
from . models import FinancialStatement

class FinancialStatementModelAdmin(admin.ModelAdmin):
	list_display 		= ["user", "date", "description", "debit","credit",  "closing_balance", "updated", "timestamp"]
	list_display_links  = ["user", "timestamp", "date"]
	# list_editable		= []
	list_filter			= ["user", "date", "timestamp"]
	search_fields		= ["user", "description"]
	class Meta:
		model = FinancialStatement


admin.site.register(FinancialStatement, FinancialStatementModelAdmin)