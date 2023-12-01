import random

def dicionario_restrições(listagem) -> None:
    for chave in listagem.keys():
        listagem[chave] = input(f'Digite o nome do servidor que possui restrição na(o) {chave}: ').split(', ')

def dicionario_fechamento(listagem) -> None:
    for chave in listagem.keys():
        listagem[chave] = input(f'Digite o nome do sevidor que vai fechar na(o) {chave}: ')

def modifica_motorista(listagem_fechamento, motoristas):
    for dia, servidor in listagem_fechamento.items():
        if servidor == motoristas[dia]:
            motoristas[dia] = 'Sergio'

def sorteio():
    for chave, lista_vagas in carro_vagas.items():
        pass

if __name__ == '__main__':
    lista_servidores = []
    restrições = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }
    fechamentos = {'segunda': '', 'terça': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sabado': '', 'domingo': '', }
    motoristas = {'segunda': 'Thiago', 'terça': 'Thiago', 'quarta': 'Thiago', 'quinta': 'Thiago', 'sexta': 'Thiago', 'sabado': 'Thiago', 'domingo': 'Thiago', }
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

    dicionario_fechamento(fechamentos)
    dicionario_restrições(restrições)
    modifica_motorista(fechamentos, motoristas)

    print(f'restrições: {restrições}\n')
    print(f'fechamento: {fechamentos}\n')
    print(f'motorista: {motoristas}\n')
    print(f'Vagas: {carro_vagas}')
