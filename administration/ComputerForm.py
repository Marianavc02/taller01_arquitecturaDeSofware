
from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['serial', 'model', 'purchase_date', 'previous_repairs']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }
