import sqlite3

def conexao():
    """
    Faz a conexão com o banco de dados.

    Returns:
        str: database Connection object
    """
    with sqlite3.connect('agenda_clientes.db') as conexao:
        return conexao.cursor()

def commit(conexao):
    """
    Confirma a query SQL no banco de dados.

    Args:
        conexao (str): database Connection object
    """
    conexao.commit()

def fechar_conexao(conexao):
    """
    Encerrar a conexão com o banco de dados.

    Args:
        conexao (str): database Connection object
    """
    conexao.close()
