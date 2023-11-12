import sqlite3

conexao = sqlite3.connect('usuario.db')

cursor = conexao.cursor()

# cursor.execute('''CREATE TABLE usuarios (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
#                                         nome_usuario TEXT NOT NULL,
#                                         idade_usuario INTEGER NOT NULL);''')

# cursor.execute("INSERT INTO usuarios (nome_usuario, idade_usuario) VALUES ('Deyved', 37)")

conexao.commit()
conexao.close()

with sqlite3.connect('usuario.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios;")
    resultado = cursor.fetchall()
    print(resultado)