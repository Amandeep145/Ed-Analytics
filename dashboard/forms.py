from django import forms




class SearchContactForm(forms.Form):
    menuname = forms.CharField(required=None)
   