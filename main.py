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
        print(f"erro ao tentar criar cadastro {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()

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

def atualizar_tabela(disponivel, id_livro):
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE livros 
        SET disponivel = ?
        WHERE id = ?
        """, (disponivel, id_livro )
        )
        conexao.commit()

    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar atulizar {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()


def remover_livros():
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()
        id = int(input("Digite o id do livro que deseja deletar: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
        conexao.commit()
        print("Livros removido com sucesso!")
    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar remover livros {erro}")


def menu():
    while True:
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar disponibilidade")
        print("4. Remover livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano do livro: ")
            cadastro_livro(titulo, autor, ano)
            print("Livro cadastrado com sucesso!")

        elif opcao == "2":
            listar_livros()

        elif opcao == "3":
            id_livro = input("Digite o ID do livro para atualizar: ")
            novo_status = input("Disponível (sim/não): ")
            atualizar_tabela(novo_status, id_livro)
            print("Disponibilidade atualizada!")
        elif opcao == "4":
            id_livro = input("Digite o ID do livro que deseja remover: ")
            remover_livro(id_livro)

        elif opcao == "5":
            print("Saindo do sistema")
            break

        else:
            print("Opção inválida. Tente novamente.")
menu()