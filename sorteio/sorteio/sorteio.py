import numpy as np
import os
import pandas as pd
import random

class Sorteio:

    def __init__(self) -> None:
        self.vaga_carro = 4

    def sorteio_vagas(self, funcionarios) -> list:
        """Faz a seleção de funcionários de acordo com a quantidade da variável da classe.

        Args:
            funcionarios (list): Conjunto de funcionários que vão participar do sorteio.

        Returns:
            list: Sorteados de acordo com a quantidade especificada.
        """
        return random.sample(funcionarios, k=self.vaga_carro)

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
    caminho = os.getcwd()

    try:
        with open(f'{caminho}\\sorteio\\arquivos\\lista_servidores.csv', 'r') as file:
            lista_servidores = file.read()
    except FileNotFoundError:
        pass

    lista_fechamento = sorteio.fechamento()
    lista_sorteio = sorteio.sorteio_vagas(lista_servidores.split(', ').copy())

    print(f'fechamento: {lista_fechamento}')
    print(f'sorteio: {lista_sorteio}')
