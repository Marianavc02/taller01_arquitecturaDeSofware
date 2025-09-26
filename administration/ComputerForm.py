from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    purchase_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    class Meta:
        serial = Computer
        model = Computer
        fields = ['serial','model', 'purchase_date', 'previous_repairs']
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_repairs': forms.Textarea(attrs={'class': 'form-control'}),
        }