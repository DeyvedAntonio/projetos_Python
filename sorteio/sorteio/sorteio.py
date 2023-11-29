import random

lista_servidores = []
restrições = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }
fechamento = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }
motorista = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }
carro_vagas = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }

with open(r'sorteio\sorteio\arquivos\lista_servidores.csv', 'r') as file:
    try:
        lista_servidores = file.read().split(', ')
    except FileNotFoundError:
        print(f'Arquivo {file} não encontrado.')
    else:
        pass

def dicionario_restrições():
    for chave in restrições.keys():
        restrições[chave] = input('Digite o nome do servidor: ').split(', ')

def dicionario_fechamento():
    for chave in fechamento.keys():
        fechamento[chave] = input('Digite o nome do sevidor: ')

def sorteio():
    for chave in carro_vagas.keys():
        pass

print(lista_servidores)
print(restrições)
