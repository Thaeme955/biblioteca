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

def cadastro_livro(titulo, autor, ano):
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
        """,  
        (titulo, autor, ano, "sim")
        )
        conexao.commit()
    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar criar tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()
            


titulo = input("Digite o titulo que você deseja: ").lower()
autor = input("Digite o nome do autor: ").lower()
ano = int(input("Digite o ano do livro: "))

cadastro_livro(titulo,autor, ano )

def listar_livros():
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM livros")

        for linha in cursor.fetchall():
            print(f"id: {linha[0]} | titulo: {linha[1]} | autor: {linha[2]} | ano: {linha[3]} | diponivel: {linha[4]}")
            print("-"*60)

    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar ver tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()

listar_livros()