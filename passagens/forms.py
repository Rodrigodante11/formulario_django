from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem:', max_length=100)
    destino = forms.CharField(label='Destino:', max_length=100)

    data_ida = forms.DateField(label='Ida:', widget=DatePicker(
        options={
            'minDate': str(datetime.today()),
            'maxDate': '2023-01-20',
        },
    ), )
    data_volta = forms.DateField(label='Volta:', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa:', disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do Voo:', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informacoes extrax:',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email:', max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_erros = {}

        campo_tem_algum_numero(origem, 'origem',  lista_erros)
        campo_tem_algum_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)

        if lista_erros is not None:  # Verifica se tem algum erro
            for erro in lista_erros:  # Para cada erro
                mensagem_erro = lista_erros[erro]  # pegando a mensagem do erro
                self.add_error(erro, mensagem_erro)  
        return self.cleaned_data
