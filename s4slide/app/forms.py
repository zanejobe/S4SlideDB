from django import forms

class databaseSearch(forms.Form):
	search = forms.CharField()
	loc = forms.BooleanField(required=False, label="Location")
	cont = forms.BooleanField(required=False, label="Contributor")
	date = forms.BooleanField(required=False)
	strat = forms.BooleanField(required=False, label="Strat Interval")
	age = forms.BooleanField(required=False)

