from django import forms
from tempus_dominus.widgets import DatePicker


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)

    data_ida = forms.DateField(label='Ida', widget=DatePicker(
        options={
            'minDate': '2009-01-20',
            'maxDate': '2023-01-20',
        },
    ),)
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
