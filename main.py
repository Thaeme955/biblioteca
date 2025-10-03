import sqlite3

def criando_tabela():
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER, 
            disponivel TEXT 
            )
        """)
    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar criar tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()

criando_tabela()
        