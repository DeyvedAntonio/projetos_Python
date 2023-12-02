import random

def dicionario_restrições(listagem) -> None:
    for chave in listagem.keys():
        listagem[chave] = input(f'Digite o nome do servidor que possui restrição na(o) {chave}: ').title().split(', ')

def dicionario_fechamento(listagem) -> None:
    for chave in listagem.keys():
        listagem[chave] = input(f'Digite o nome do sevidor que vai fechar na(o) {chave}: ').title()

def modifica_motorista(listagem_fechamento, motoristas):
    for dia, servidor in listagem_fechamento.items():
        if servidor == motoristas[dia]:
            motoristas[dia] = 'Sergio'

def sorteio(carro_vagas, restricoes, fechamento, lista_servidores):
    for chave, lista_vagas in carro_vagas.items():
        for vaga in lista_vagas.keys():
            sair = False
            while sair != True:
                sorteado = random.choice(lista_servidores)
                verificado = verifica_restrições(sorteado, restricoes, fechamento)
                if verificado:
                    continue
                else:
                    carro_vagas[chave][vaga] = sorteado
                    sair = True

def verifica_restrições(sorteado: str, restricoes: dict, fechamento: dict) -> bool:
    if sorteado in restricoes or sorteado in fechamento:
        return True
    else:
        return False

if __name__ == '__main__':
    lista_servidores = []
    restricoes = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': [], }
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
    dicionario_restrições(restricoes)
    modifica_motorista(fechamentos, motoristas)
    sorteio(carro_vagas, restricoes, fechamentos, lista_servidores)

    print(f'restrições: {restricoes}\n')
    print(f'fechamento: {fechamentos}\n')
    print(f'motorista: {motoristas}\n')
    print(f'Vagas: {carro_vagas}')
