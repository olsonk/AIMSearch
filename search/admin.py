from django.contrib import admin
from search.models import Issue, Activity, Standard

class ActivityAdmin(admin.ModelAdmin):
	list_display = ('issue', 'title')

# Register your models here.
admin.site.register(Issue)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Standard)