from django import forms
from .models import Query

class UserForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['keyword','industry','year_founded','state','country','total_emp','current_emp',]
