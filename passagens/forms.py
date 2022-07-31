from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa:', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de Ida',
            'data_volta': 'Data de Volta',
            'classe_viagem': 'Classe de viagem'
        }
        options = {
            'minDate': str(datetime.today()),
            'maxDate': '2023-01-20',
        }
        widgets = {
            'data_ida': DatePicker(options=options),
            'data_volta': DatePicker(options=options)
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        destino = self.cleaned_data.get('destino')
        lista_erros = {}

        campo_tem_algum_numero(origem, 'origem', lista_erros)
        campo_tem_algum_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        data_id_maior_que_data_volta(data_ida, data_volta, lista_erros)

        if lista_erros is not None:  # Verifica se tem algum erro
            for erro in lista_erros:  # Para cada erro
                mensagem_erro = lista_erros[erro]  # pegando a mensagem do erro
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email']  # operand o campo email
        exclude = ['nome']  # pegando todos os campos menos o 'nome'
