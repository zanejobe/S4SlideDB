from django import forms

class databaseSearch(forms.Form):
	name = forms.CharField(required=False)
	cont = forms.CharField(required=False, label="Contributor")
	lat_start = forms.DecimalField(required=False, label="Starting Latitude", min_value=-90, max_value=90)
	lat_end = forms.DecimalField(required=False, label="Ending Latitude", min_value=-90, max_value=90)
	lng_start = forms.DecimalField(required=False, label="Starting Longitude", min_value=-180, max_value=180)
	lng_end = forms.DecimalField(required=False, label="Ending Longitude", min_value=-180, max_value=180)
	date_start = forms.DateField(required=False, label="Starting Upload Date")
	date_end = forms.DateField(required=False, label="Ending Upload Date")
	age = forms.CharField(required=False, label="Age Period")

	def clean(self):
		cleaned_data = super().clean()
		
		all_empty = True
		for v in cleaned_data.values():
			if v:
				all_empty = False
				break
		if all_empty:
			raise forms.ValidationError("One or more fields must have a valid input.")

		if cleaned_data["lat_start"] and not cleaned_data["lat_end"]:
			self.add_error("lat_end", "You must specify an ending latitude.")
		elif not cleaned_data["lat_start"] and cleaned_data["lat_end"]:
			self.add_error("lat_start", "You must specify a starting latitude.")
		if cleaned_data["lng_start"] and not cleaned_data["lng_end"]:
			self.add_error("lng_end", "You must specify an ending longitude.")
		elif not cleaned_data["lng_start"] and cleaned_data["lng_end"]:
			self.add_error("lng_start", "You must specify a starting longitude.")

		return cleaned_data

