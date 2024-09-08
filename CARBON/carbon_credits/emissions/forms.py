from django import forms
from .models import CoalMine, Tree

class CoalMineForm(forms.ModelForm):
    class Meta:
        model = CoalMine
        fields = ['name', 'location', 'total_coal_extracted', 'emission_factor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'total_coal_extracted': forms.NumberInput(attrs={'class': 'form-control'}),
            'emission_factor': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['name', 'carbon_absorption_rate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'carbon_absorption_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
