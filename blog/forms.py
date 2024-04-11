from django import forms
from .models import *
class MapForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name','phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام و نام خانوادگی"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "شماره تلفن"})
        }



