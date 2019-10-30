from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model=Page
        fields=['title','content','order'] # deben ser los mismos del modelo
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'order':forms.NumberInput(attrs={'class':'form-control'}),
        }

class PageEditForm(forms.ModelForm):
    class Meta:
        model=Page
        fields = ['title','content','order'] # deben ser los mismos del modelo
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'order':forms.NumberInput(attrs={'class':'form-control'}),
        }
