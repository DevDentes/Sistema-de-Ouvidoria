from operacoesbd import *

conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')

consulta = 'select * from manifestacoes'
manifestacoes = listarBancoDados(conn, consulta)

if len (manifestacoes) ==0:
    print ("Sem manifestacoes")
else:
    print("Lista de Manifestações")
    for item in manifestacoes:
        print(item[0],"-", "Tipo:", item[1], "Descrição:", item[2], "Postada no dia:", item[3])

        encerrarConexao(conn)