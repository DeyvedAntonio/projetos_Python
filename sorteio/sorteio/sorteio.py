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
        lista_servidores = file.read()
except FileNotFoundError:
    pass

def definir_fechamento():
    for chave in lista_fechamento.keys():
        lista_fechamento[chave] = input(f'Informe o nome do servidor responsável pelo fechamento no(a) {chave} ').strip().title()

def definir_motorista():
    for chave in motoristas.keys():
        motoristas[chave] = input(f'Infome o motorista no(a) {chave} ').strip().title()

def sorteio_nomes(quantidade=vagas_carro):
    sorteados = random.choices(lista_servidores, k=quantidade)

def verificar_fechamento(nomes):
    pass

definir_fechamento()

sorteio_nomes()
