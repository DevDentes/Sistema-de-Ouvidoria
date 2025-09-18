from operacoesbd import *
import datetime

conn = criarConexao('localhost', 'root', '7612', 'sgbd_ouvidoria')

tipoManifestacao = input("Digite o tipo da sua Manifestacao: ")
descricaoManifestacao = input("Digite a sua Manifestacao: ")
data = input("Digite a data da manifestação (YYYY-MM-DD): ")
consulta = 'insert into manifestacoes (tipo, descricao, data_criacao) values (%s, %s, %s) '
data = datetime.date.today()
valores = [tipoManifestacao, descricaoManifestacao, data]

codigo = insertNoBancoDados(conn, consulta,  valores )
print ("Manifestação adicionada com sucesso! Manifestação Numero: ", codigo)

encerrarConexao(conn)