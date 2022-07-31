def origem_destino_iguais(origem, destino, lista_de_erros):
    """
    Verifica se orige e destino sao igauis
    :param origem:
    :param destino:
    :param lista_de_erros:
    :return:
    """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino nao podem ser iguais'
        # lista_de_erros['campo que vai aparece o erro']


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """
    Verifica se possui algum digito Numerico

    :param valor_campo:
    :param nome_campo:
    :param lista_de_erros:
    :return:
    """
    if any(char.isdigit() for char in valor_campo):  # Verificando se um dos caracteres eh digito
        lista_de_erros[nome_campo] = 'Nao inclua Numeros!'
