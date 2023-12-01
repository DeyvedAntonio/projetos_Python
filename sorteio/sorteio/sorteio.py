import random

lista_servidores = []
restrições = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }
fechamento = {'segunda': '', 'terça': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sabado': '', 'domingo': '', }
motorista = {'segunda': 'Thiago', 'terça': 'Thiago', 'quarta': 'Thiago', 'quinta': 'Thiago', 'sexta': 'Thiago', 'sabado': 'Thiago', 'domingo': 'Thiago', }
carro_vagas = {'segunda': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
               'terça': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
               'quarta': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
               'quinta': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
               'sexta': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
               'sabado': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
               'domingo': {'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, }

with open(r'sorteio\sorteio\arquivos\lista_servidores.csv', 'r') as file:
    try:
        lista_servidores = file.read().split(', ')
    except FileNotFoundError:
        print(f'Arquivo {file} não encontrado.')
    else:
        pass

def dicionario_restrições() -> None:
    for chave in restrições.keys():
        restrições[chave] = input(f'Digite o nome do servidor que possui restrição na(o) {chave}: ').split(', ')

def dicionario_fechamento() -> None:
    for chave in fechamento.keys():
        fechamento[chave] = input(f'Digite o nome do sevidor que vai fechar na(o) {chave}: ')

def modifica_motorista():
    for dia, servidor in fechamento.items():
        if servidor == motorista[dia]:
            motorista[dia] = 'Sergio'

def sorteio():
    for chave in carro_vagas.keys():
        pass

if __name__ == '__main__':
    dicionario_fechamento()
    dicionario_restrições()
    modifica_motorista()

    print(f'restrições: {restrições}\n')
    print(f'fechamento: {fechamento}\n')
    print(f'motorista: {motorista}\n')
    print(f'Vagas: {carro_vagas}')
