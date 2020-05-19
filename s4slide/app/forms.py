from django import forms

class databaseSearch(forms.Form):
    search = forms.CharField()
    loc = forms.CheckboxInput()
    cont = forms.CheckboxInput()
    date = forms.CheckboxInput()
    strat = forms.CheckboxInput()
    age = forms.CheckboxInput()
    loc2 = forms.CheckboxInput()