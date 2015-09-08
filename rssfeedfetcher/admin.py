from django.contrib import admin

# Register your models here.
from .models import feedUrl

class RssAdmin(admin.ModelAdmin):
	class Meta:
		model = feedUrl

admin.site.register(feedUrl, RssAdmin)