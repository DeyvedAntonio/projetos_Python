import pandas as pd
import numpy as np
import random

class Sorteio:
    vaga_carro = 4

    def __init__(self) -> None:
        pass

    def sorteio_vagas(self, servidores, fechamento):
        flag = False
        carro_vagas = {'segunda': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', }, 
                       'terça': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', }, 
                       'quarta': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', }, 
                       'quinta': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', }, 
                       'sexta': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', }, 
                       'sábado': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', }, 
                       'domingo': {'vaga_1': '', 'vaga_2': '', 'vaga_3': '', 'vaga_4': '', },}

    def fechamento(self) -> dict:
        """
        Criar uma lista de fechamento do cartório.
        Returns:
            dict: lista de fechamento - dia e pessoa
        """
        lista_fechamento = {'segunda': '', 'terça': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sábado': '', 'domingo': '',}
        for dia in lista_fechamento.keys():
            lista_fechamento[dia] = input(f'Informe a pessoa responsável pelo fechamento do cartório no(a) {dia}: ').strip().title()
        return lista_fechamento


if '__main__' == __name__:
    sorteio = Sorteio()
    lista_servidores = []

    try:
        with open(r'arquivos\lista_servidores.csv') as file:
            lista_servidores = file.read()
    except FileNotFoundError:
        pass

    lista_fechamento = sorteio.fechamento()
    lista_sorteio = sorteio.sorteio_vagas(lista_servidores.copy(), lista_fechamento)
