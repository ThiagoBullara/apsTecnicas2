import os
import sys

listaDeUsuarios = [
    {"nome": "Thiago", "sobrenome": "Bullara", "email": "21361619@anhembi.com.br"}, 
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
    novoUsuario["nome"] = input("\nDigite o primeiro nome do usuário: ")
    novoUsuario["sobrenome"] = input("Digite o sobrenome do usuário: ")
    novoUsuario["email"] = input("Digite o email do usuário: ")
    return novoUsuario

def listarUsuariosOrdemCadastro():

    print("\nNome dos usuários por ordem de cadastro:")

    for usuario in listaDeUsuarios:
       for nome in usuario.keys():
            if(nome == "nome"):
                print("\nUsuário número {} = ".format(listaDeUsuarios.index(usuario)),usuario["nome"] + " " + usuario["sobrenome"], "/ Email:", usuario["email"])

def listarUsuariosOrdemAlfabetica():

    listaEmORdemAlfabetica = []

    for usuario in listaDeUsuarios:
           for nome in usuario.keys():
            if(nome == "nome"):
                listaEmORdemAlfabetica.append(usuario["nome"])

    listaEmORdemAlfabetica.sort()
    print("\nLista de usuários em ordem Alfabética\n")

    for usuario in listaEmORdemAlfabetica:
        print(usuario, "\n")

def buscarPeloNome():
    
    flag = 0
    nomePesquisar = input("\nInsira o primeiro nome do usuário que deseja buscar: ")

    for usuario in listaDeUsuarios:
        for nome in usuario.values():
            if nomePesquisar == nome:
                print("\nUsuário encontrado: ",usuario)
                flag = 1

    if flag == 0:
        print("\nUsuário não encontrado")

def removerUsuario():
    
    flag = 0
    emailPesquisar = input("\nInsira o email do usuário que deseja remover da lista: ")

    for usuario in listaDeUsuarios:
        for email in usuario.values():
            if emailPesquisar == email:
                print("\nO seguinte usuário vai ser removido: ", usuario)
                input("\nAperte ENTER para continuar")
                listaDeUsuarios.remove(usuario)
                print("\nUsuário removido com sucesso!!")
                flag = 1

    if flag == 0:
        print("\nUsuário não encontrado")

def atualizarDados():

    flag = 0
    emailPesquisar = input("\nInsira o email do usuário para poder atualizar seu nome: ")

    for usuario in listaDeUsuarios:
        for email in usuario.values():
            if emailPesquisar == email:
                print("\nUsuário encontrado, nome atual:",usuario["nome"])
                usuario["nome"] = input("\nInsira o novo nome: ")
                print("\nNome do usuário atualizado com sucesso!!")
                flag = 1

    if flag == 0:
        print("\nUsuário não encontrado")

def main():
    
    menu()

    opcao = int(input("Selecione uma opcao: "))

    if opcao == 0 or opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7:
        while opcao != 0: 
            if opcao == 1:
                umUsuario = cadastroDeUsuario()
                listaDeUsuarios.append(umUsuario)
                print("\nUsuário cadastrado com sucesso!!")
                input("\nAperte ENTER para continuar")
                opcao = 7
                limparConsole()
            elif opcao == 2:
                listarUsuariosOrdemCadastro()
                input("\nAperte ENTER para continuar")
                opcao = 7
                limparConsole()
            elif opcao == 3:
                listarUsuariosOrdemAlfabetica()
                input("Aperte ENTER para continuar")
                opcao = 7
                limparConsole()
            elif opcao == 4:
                buscarPeloNome()
                input("\nAperte ENTER para continuar")
                opcao = 7
                limparConsole()
            elif opcao == 5:
                removerUsuario()
                input("\nAperte ENTER para continuar")
                opcao = 7
                limparConsole()
            elif opcao == 6:
                atualizarDados()
                input("\nAperte ENTER para continuar")
                opcao = 7
                limparConsole()
            elif opcao == 7:
                main()
        print("\nSistema encerrado")
        sys.exit()
    else: 
        print("\nInsira uma opção válida")
        input("\nAperte Enter para continuar")
        limparConsole()
        main()

if __name__ == "__main__":
        main()