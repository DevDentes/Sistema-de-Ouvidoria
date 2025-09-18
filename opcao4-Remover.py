from operacoesbd import *

conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')

codigo = int(input("Digite o codigo da maniofestação a ser removida: "))

consulta = 'delete from manifestacoes where codigo = %s'
valores = [ codigo ]

manifestacaoRemovida = excluirBancoDados(conn, consulta, valores)

if manifestacaoRemovida >= 1:
    print("A manifestação foi removida com sucesso!")

else:
    print("O codigo informado é invalido.")