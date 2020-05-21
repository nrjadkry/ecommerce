from django import forms

class EmailForm(forms.Form):
	email=forms.CharField(required=True)
	password=forms.CharField(required=True)
	toemail=forms.CharField(required=True)
	bcc=forms.CharField(required=False)
	cc=forms.CharField(required=False)
	subject=forms.CharField(required=False)
	body=forms.CharField(required=False)
	file=forms.FileField(required=False)
	repetition=forms.IntegerField(required=False)

