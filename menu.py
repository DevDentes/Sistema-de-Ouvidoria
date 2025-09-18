from operacoesbd import *

conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')

opcao = 1

manifestacao = [ ]

while opcao != 6:
    print("\nOuvidoria")
    print ("1) Listar Manifestação \n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Remover Manifetação \n5) Substituir Manifetação \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        print("Listar Manifetação")

    elif opcao == 2:
        print("Adicionar Manifestação")

    elif opcao == 3:
        print("Pesquisar Manifestação")

    elif opcao == 4:
        print("Remover Manifestação")

    elif opcao == 5:
        print("Substituir Manifestação")

    elif opcao != 6:
        print("Opção Invalida")

    encerrarConexao(conn)

    print("Obrigado por usar a Ouvidoria!")
