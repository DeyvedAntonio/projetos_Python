import os
import random

vagas_carro = 4
caminho = os.getcwd()
lista_fechamento = {'segunda': '', 'terca': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sabado': '', 'domingo': '',}
lista_vagas = {'segunda': [], 'terca': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [],}
restricoes = {'segunda': [], 'terca': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [],}
lista_servidores = []
motoristas = {'segunda': '', 'terca': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sabado': '', 'domingo': '',}

try:
    with open(f'{caminho}\\sorteio\\arquivos\\lista_servidores.csv', 'r') as file:
        lista_servidores = file.read().split(', ')
except FileNotFoundError:
    pass

def definir_fechamento():
    for chave in lista_fechamento.keys():
        lista_fechamento[chave] = input(f'Informe o nome do servidor responsável pelo fechamento no(a) {chave} ').strip().title()

def definir_motorista():
    for chave in motoristas.keys():
        motoristas[chave] = input(f'Infome o motorista no(a) {chave} ').strip().title()

def sorteio_nomes(quantidade=vagas_carro):
    return random.sample(lista_servidores, k=quantidade)

def verificar_fechamento(nome: str):
    for v in lista_fechamento.values():
        if nome == v:
            return True
        else:
            return False

definir_fechamento()

for key in lista_vagas.keys():
    sorteados = sorteio_nomes()
    for nome in sorteados:
        confirmacao = verificar_fechamento(nome)
        if confirmacao == True:
            sorteados.pop(nome)
    if len(sorteados) < vagas_carro:
        # TODO: novo sorteio com a quantidade que falta
        pass
