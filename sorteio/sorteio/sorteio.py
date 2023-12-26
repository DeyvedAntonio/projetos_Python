import os
import random

vagas_carro = 4
caminho = os.getcwd()
lista_fechamento = {'segunda': '', 'terca': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sabado': '', 'domingo': '',}
lista_servidores = []

try:
    with open(f'{caminho}\\sorteio\\arquivos\\lista_servidores.csv', 'r') as file:
        lista_servidores = file.read()
except FileNotFoundError:
    pass

def definir_fechamento():
    for chave in lista_fechamento.keys():
        lista_fechamento[chave] = input(f'Informe o nome do servidor responsável pelo fechamento no(a) {chave} ').strip().title()

def sorteio_nomes(quantidade=vagas_carro):
    sorteados = random.choices(lista_servidores, k=quantidade)


definir_fechamento()
sorteio_nomes()
