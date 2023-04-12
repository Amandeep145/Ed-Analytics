from django import forms
from django.db.models import fields
from .models import role_master, menu_master1, role_menu_map, user_map

  




class roleForm(forms.ModelForm):
    class Meta:
        model = role_master
        fields = ('rolename','rolecode','roledesc','status')
    def __init__(self, *args, **kwargs):
        super(roleForm, self).__init__(*args, **kwargs)

class menuForm(forms.ModelForm):
    class Meta:
        model = menu_master1
        fields = ('menuname','menuurl','menudesc','status','menu_parent','iconn')
    def __init__(self, *args, **kwargs):
        super(menuForm, self).__init__(*args, **kwargs)        

class SearchContactForm(forms.Form):
    rolename = forms.CharField(required=None)
    menuname = forms.CharField(required=None)
    role_master = forms.CharField(required=None)
    user_master = forms.CharField(required=None)


class role_menu_mapForm(forms.ModelForm):
    class Meta:
        model = role_menu_map
        fields = ('role_master','menu_master')
    def __init__(self, *args, **kwargs):
        super(role_menu_mapForm, self).__init__(*args, **kwargs)



class user_mapForm(forms.ModelForm):
    class Meta:
        model = user_map
        fields = ('role_master','user_master')
    def __init__(self, *args, **kwargs):
        super(user_mapForm, self).__init__(*args, **kwargs)
