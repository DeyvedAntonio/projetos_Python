import sqlite3

def conexao():
    return sqlite3.connect('agenda_clientes.db')

def cursor(con):
    return con.cursor()

def commit(conexao):
    conexao.commit()

def fechar_conexao(conexao):
    conexao.close()
