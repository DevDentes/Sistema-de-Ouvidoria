from operacoesbd import *
from metodos import *

opcao = 1
conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')


manifestacao = [ ]

while opcao != 6:
    print("\nOuvidoria")
    print ("1) Listar Manifestação \n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Remover Manifetação \n5) Quantidade de manifestações \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        listarTodos(conn)

    elif opcao == 2:
        adicionarManifestacao(conn)

    elif opcao == 3:
        pesquisarManifestacao(conn)

    elif opcao == 4:
        removerManifestacao(conn)

    elif opcao == 5:
        quantidadeManifestacao(conn)

    elif opcao != 6:
        print("Opção Invalida")

    print("Obrigado por usar a Ouvidoria!")