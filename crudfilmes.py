## Listas para armazenar dados
diretores = []
filmes = []

## CRUD DIRETOR
def criar_diretor(id_diretor, nome):
    diretor = {"id_diretor": id_diretor, "nome": nome}
    diretores.append(diretor)
    print("Diretor criado com sucesso!")

def ler_diretor(id_diretor):
    for diretor in diretores:
        if diretor["id_diretor"] == id_diretor:
            return diretor
    return None

def atualizar_diretor(id_diretor, novo_nome):
    diretor = ler_diretor(id_diretor)
    if diretor:
        diretor["nome"] = novo_nome
        print("Diretor atualizado com sucesso!")
    else:
        print("Diretor não encontrado.")

def deletar_diretor(id_diretor):
    diretor = ler_diretor(id_diretor)
    if diretor:
        diretores.remove(diretor)
        print("Diretor deletado com sucesso!")
    else:
        print("Diretor não encontrado.")

## CRUD FILMES
def criar_filme(id_filme, titulo, id_diretor):
    if ler_diretor(id_diretor):
        filme = {"id_filme": id_filme, "titulo": titulo, "id_diretor": id_diretor}
        filmes.append(filme)
        print("Filme criado com sucesso!")
    else:
        print("Diretor não encontrado. Criação de filme falhou.")

def ler_filme(id_filme):
    for filme in filmes:
        if filme["id_filme"] == id_filme:
            return filme
    return None

def atualizar_filme(id_filme, novo_titulo, novo_id_diretor):
    filme = ler_filme(id_filme)
    if filme:
        if ler_diretor(novo_id_diretor):
            filme["titulo"] = novo_titulo
            filme["id_diretor"] = novo_id_diretor
            print("Filme atualizado com sucesso!")
        else:
            print("Novo diretor não encontrado. Atualização de filme falhou.")
    else:
        print("Filme não encontrado.")

def deletar_filme(id_filme):
    filme = ler_filme(id_filme)
    if filme:
        filmes.remove(filme)
        print("Filme deletado com sucesso!")
    else:
        print("Filme não encontrado.")

## Funções para listar os dados

def listar_diretores():
    if diretores:
        print("\nDiretores:")
        for diretor in diretores:
            print(f"ID: {diretor['id_diretor']}, Nome: {diretor['nome']}")
    else:
        print("\nNenhum diretor encontrado.")

def listar_filmes():
    if filmes:
        print("\nFilmes:")
        for filme in filmes:
            print(f"ID: {filme['id_filme']}, Título: {filme['titulo']}, ID Diretor: {filme['id_diretor']}")
    else:
        print("\nNenhum filme encontrado.")
        
## MENU
def menu():
    while True:
        listar_diretores()
        listar_filmes()

        print("\nMenu:")
        print("1. Criar Diretor")
        print("2. Ler Diretor")
        print("3. Atualizar Diretor")
        print("4. Deletar Diretor")
        print("5. Criar Filme")
        print("6. Ler Filme")
        print("7. Atualizar Filme")
        print("8. Deletar Filme")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_diretor = int(input("ID do Diretor: "))
            nome = input("Nome do Diretor: ")
            criar_diretor(id_diretor, nome)
        elif opcao == "2":
            id_diretor = int(input("ID do Diretor: "))
            diretor = ler_diretor(id_diretor)
            if diretor:
                print(f"ID: {diretor['id_diretor']}, Nome: {diretor['nome']}")
            else:
                print("Diretor não encontrado.")
        elif opcao == "3":
            id_diretor = int(input("ID do Diretor: "))
            novo_nome = input("Novo Nome do Diretor: ")
            atualizar_diretor(id_diretor, novo_nome)
        elif opcao == "4":
            id_diretor = int(input("ID do Diretor: "))
            deletar_diretor(id_diretor)
        elif opcao == "5":
            id_filme = int(input("ID do Filme: "))
            titulo = input("Título do Filme: ")
            id_diretor = int(input("ID do Diretor do Filme: "))
            criar_filme(id_filme, titulo, id_diretor)
        elif opcao == "6":
            id_filme = int(input("ID do Filme: "))
            filme = ler_filme(id_filme)
            if filme:
                print(f"ID: {filme['id_filme']}, Título: {filme['titulo']}, ID Diretor: {filme['id_diretor']}")
            else:
                print("Filme não encontrado.")
        elif opcao == "7":
            id_filme = int(input("ID do Filme: "))
            novo_titulo = input("Novo Título do Filme: ")
            novo_id_diretor = int(input("Novo ID do Diretor do Filme: "))
            atualizar_filme(id_filme, novo_titulo, novo_id_diretor)
        elif opcao == "8":
            id_filme = int(input("ID do Filme: "))
            deletar_filme(id_filme)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()