import random

def dicionario_restrições(listagem: list) -> None:
    for chave in listagem.keys():
        listagem[chave] = input(f'Digite o nome do servidor que possui restrição na(o) {chave}: ').title().split(', ')

def dicionario_fechamento(listagem: list) -> None:
    for chave in listagem.keys():
        listagem[chave] = input(f'Digite o nome do sevidor que vai fechar na(o) {chave}: ').title()

def modifica_motorista(dia: str, motorista: str, substituto: str) -> str:
    """
    seleciona o motorista de acordo com a restrição do dia que o motorista é o responsável pelo fechamento.

    Args:
        dia (str): responsável pelo fechamento.
        motorista (str): motorista principal do carro.
        substituto (str): motorista substituto.

    Returns:
        str: retorna quem pode ser o motorista de acordo com os critários.
    """
    if dia != motorista:
        return motorista
    else:
        return substituto

def sorteio(carro_vagas: dict, restricoes: dict, fechamento: dict, lista_servidores: list, limite: dict, motorista: str, substituto: str):
    for chave, lista_vagas in carro_vagas.items():
        for vaga in lista_vagas.keys():
            sair = False
            while sair != True:
                if vaga == 'MO':
                    carro_vagas[chave][vaga] = modifica_motorista(fechamento[chave], motorista, substituto)
                    sair = True
                    continue
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

def informar_motorista() -> str:
    return str(input('Informe quem será o motorista: ').title())
    
def informar_substituto() -> str:    
    return str(input('Informe quem será o motorista substituto: ').title())


def verifica_quantidade(nome, quantidade):
    pass

if __name__ == '__main__':
    lista_servidores = []
    restricoes = {'segunda': [], 'terça': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sábado': [], 'domingo': [], }
    fechamentos = {'segunda': '', 'terça': '', 'quarta': '', 'quinta': '', 'sexta': '', 'sábado': '', 'domingo': '', }
    carro_vagas = {'segunda': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
                'terça': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
                'quarta': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
                'quinta': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
                'sexta': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
                'sábado': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, 
                'domingo': {'MO': '', 'Vaga1': '', 'Vaga2': '', 'Vaga3': '', 'Vaga4': ''}, }

    with open(r'sorteio\arquivos\lista_servidores.csv', 'r') as file: # D:\Mega\00.Portifolio\projetos_Python\sorteio\sorteio\arquivos\lista_servidores.csv
        try:
            lista_servidores = file.read().split(', ')
        except FileNotFoundError:
            print(f'Arquivo {file} não encontrado.')
        else:
            pass

    total_vaga = 4 * 7
    limite_sorteio = {(nome, 0) for nome in lista_servidores}
    dicionario_fechamento(fechamentos)
    dicionario_restrições(restricoes)
    motorista = informar_motorista()
    substituto = informar_substituto()
    sorteio(carro_vagas, restricoes, fechamentos, lista_servidores, limite_sorteio, motorista, substituto)

    print(f'restrições: {restricoes}\n')
    print(f'fechamento: {fechamentos}\n')
    print(f'motorista: {motorista}\n')
    print(f'motorista substituto: {substituto}\n')
    print(f'Vagas: {carro_vagas}\n')
    print(f'QTD sorteio: {limite_sorteio}')
