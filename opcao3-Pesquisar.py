from operacoesbd import *

conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')

codigo = int(input("Digite o código da manifestação a ser pesquisada: "))

consulta = 'select * from manifestacoes where codigo = %s '
valores = [ codigo ]
manifestacoes = listarBancoDados(conn, consulta, valores)

if len (manifestacoes) ==0:
    print ("Código invalido")
else:
    print("A manisfestação pesquisada foi:")
    for item in manifestacoes:
        print(item[0], "-", "Tipo:", item[1], "Descrição:", item[2], "Postada no dia:", item[3])

encerrarConexao(conn)
