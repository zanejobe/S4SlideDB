from django.contrib import admin
from .models import *

def verify(modeladmin, request, queryset):
	queryset.update(verified=True)
verify.short_description = "Verify selected rows"

def unverify(modeladmin, request, queryset):
	queryset.update(verified=False)
unverify.short_description = "Unverify selected rows"

class MetaAdmin(admin.ModelAdmin):
	date_hierarchy = "upload_date"
	list_display = ("landslide", "data_type", "data_source", "contact_name", "contact_email")
	list_filter = ("verified",)
	actions = [verify, unverify]

	def delete_queryset(self, request, queryset):
		summary_info_id.objects.filter(id__in=queryset).delete()

	def delete_model(self, request, obj):
		self.delete_queryset(request, [obj.landslide.id])

admin.site.register(meta_table, MetaAdmin)
