from .infra.conexao import *

def verificar_usuario(nome, chave):
    con = conexao()
    resultado = con.execute(f"SELECT user_cliente FROM clientes WHERE user_cliente = {nome};")
    if resultado.fetchall is None:
        return 'Usuário não localizado.'
