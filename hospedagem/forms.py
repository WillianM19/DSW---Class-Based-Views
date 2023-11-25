from django import forms
from .models import Hospedagem
from django.forms import ModelForm

class HospedagemForm(ModelForm):
    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = {
            'data_entrada' : forms.DateInput(attrs={'class': 'form-control' }),
            'data_saida' : forms.DateInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }),
            'cliente': forms.Select(attrs={'class': 'form-control' }),
            'quarto': forms.Select(attrs={'class': 'form-control' })
        }