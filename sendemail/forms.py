from django.forms import ModelForm
from django import forms

class EmailForm(forms.Form):
	class Meta:
		fields = ['email', 'subject', 'body']

