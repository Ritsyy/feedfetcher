from django import forms

from .models import feedUrl

class FeedUrlForm(forms.ModelForm):
		class Meta:
			model = feedUrl
			fields = '__all__'