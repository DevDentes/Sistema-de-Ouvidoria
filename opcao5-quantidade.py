from operacoesbd import *

conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')

consulta = "select count(*) from manifestacoes"
manifestacoes = listarBancoDados(conn, consulta)

print(manifestacoes[0][0])

encerrarConexao(conn)