from infra.conexao import *

def verificar_usuario(nome, chave):
    cursor = conexao()
    resultado = cursor.execute(f"SELECT user_cliente FROM clientes WHERE user_cliente = '{nome}'")
    return resultado.fetchall()
