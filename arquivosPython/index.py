# Array dentro de array com: nome, sobrenome e email H1 XX
# Exibir usuários cadastrados por ordem de cadastro H2 XX
# Exibir usuários cadastrados por ordem alfabética H3 XX
# Buscar usuário pelo nome H4 XX
# Remover usuário pelo email ou pelo nome H5
# Atualizar dados do usuário buscando pelo email H6

import os

listaDeUsuarios = [
    {"nome": "Thiago", "Sobrenome": "Bullara", "email": "21361619@anhembi.com.br"}, 
    {"nome": "Guilherme", "sobrenome": "Cabral de Moura", "email": "21601989@anhembimorumbi.edu.br"},
    {"nome": "Tiago", "sobrenome": "Klein", "email": "21631075@anhembimorumbi.edu.br"}
    ]

def limparConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\nBem vindo ao sistema de gerenciamento de processos de inscrição\n")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários por ordem de cadastro")
    print("3 - Listar usuários por ordem alfabética")
    print("4 - Verificar se o usuário está inscrito")
    print("5 - Remover usuário")
    print("6 - Atualizar dados de usuário")
    print("0 - Sair do sistema\n")

def cadastroDeUsuario():
    novoUsuario = {}
    novoUsuario["nome"] = input("\nDigite o nome do usuário: ")
    novoUsuario["sobrenome"] = input("Digite o sobrenome do usuário: ")
    novoUsuario["email"] = input("Digite o email do usuário: ")
    return novoUsuario

def listarUsuariosOrdemCadastro():

    print("\nNome dos usuários por ordem de cadastro:")

    for usuario in listaDeUsuarios:
       for nome in usuario.keys():
            if(nome == "nome"):
                print("\nUsuário número {} = ".format(listaDeUsuarios.index(usuario)),usuario["nome"])

def listarUsuariosOrdemAlfabetica():

    listaEmORdemAlfabetica = []

    for usuario in listaDeUsuarios:
           for nome in usuario.keys():
            if(nome == "nome"):
                listaEmORdemAlfabetica.append(usuario["nome"])

    listaEmORdemAlfabetica.sort()
    print("\nLista de usuários em Orde Alfabética\n")

    for usuario in listaEmORdemAlfabetica:
        print(usuario, "\n")

def buscarPeloNome():
    
    flag = 0
    nomePesquisar = input("\nInsira o nome do usuário que deseja buscar: ")

    for usuario in listaDeUsuarios:
        for nome in usuario.values():
            if nomePesquisar == nome:
                print("\nUsuário encontrado: ",usuario)
                flag = 1

    if flag == 0:
        print("\nUsuário não encontrado")

def main():
    menu()

    opcao = int(input("Selecione uma opcao: "))

    while opcao != 0: 
        if opcao == 1:
            umUsuario = cadastroDeUsuario()
            listaDeUsuarios.append(umUsuario)
            print("\nUsuário cadstrado com sucesso!!")
            input("\nAperte Enter para continuar")
            opcao = 7
            limparConsole()
        elif opcao == 2:
            listarUsuariosOrdemCadastro()
            input("\nAperte Enter para continuar")
            opcao = 7
            limparConsole()
        elif opcao == 3:
            listarUsuariosOrdemAlfabetica()
            input("\nAperte Enter para continuar")
            opcao = 7
            limparConsole()
        elif opcao == 4:
            buscarPeloNome()
            input("\nAperte Enter para continuar")
            opcao = 7
            limparConsole()
        elif opcao == 7:
            main()

if __name__ == "__main__":
    main()