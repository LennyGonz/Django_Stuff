from django import forms

class FormName(forms.Form):
    #form attributes
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
