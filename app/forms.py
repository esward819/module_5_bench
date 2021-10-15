from django import forms
class SumForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
    z = forms.IntegerField()