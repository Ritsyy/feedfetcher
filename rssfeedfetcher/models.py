from django.db import models
from django.forms import ModelForm
from django.utils.encoding import smart_unicode

# Create your models here.
class feedUrl(models.Model):
	url = models.CharField(max_length=300, null = True, blank = False, unique = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	id = models.AutoField(primary_key=True)

	def __unicode__(self):
		return smart_unicode(self.url)