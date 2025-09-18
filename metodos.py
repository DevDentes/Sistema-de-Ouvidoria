from operacoesbd import *
import datetime

def listarTodos(conn):
    consulta = 'select * from manifestacoes'
    manifestacoes = listarBancoDados(conn, consulta)

    if len(manifestacoes) == 0:
        print("Sem manifestacoes")
    else:
        print("Lista de Manifestações")
        for item in manifestacoes:
            print(item[0], "-", "Tipo:", item[1], "Descrição:", item[2], "Postada no dia:", item[3])


def adicionarManifestacao(conn):
    tipoManifestacao = input("Digite o tipo da sua Manifestacao: ")
    descricaoManifestacao = input("Digite a sua Manifestacao: ")
    data = input("Digite a data da manifestação (YYYY-MM-DD): ")
    consulta = 'insert into manifestacoes (tipo, descricao, data_criacao) values (%s, %s, %s) '
    data = datetime.date.today()
    valores = [tipoManifestacao, descricaoManifestacao, data]

    codigo = insertNoBancoDados(conn, consulta, valores)
    print("Manifestação adicionada com sucesso! Manifestação Numero: ", codigo)

def pesquisarManifestacao(conn):
    codigo = int(input("Digite o código da manifestação a ser pesquisada: "))

    consulta = 'select * from manifestacoes where codigo = %s '
    valores = [codigo]
    manifestacoes = listarBancoDados(conn, consulta, valores)

    if len(manifestacoes) == 0:
        print("Código invalido")
    else:
        print("A manisfestação pesquisada foi:")
        for item in manifestacoes:
            print(item[0], "-", "Tipo:", item[1], "Descrição:", item[2], "Postada no dia:", item[3])

def removerManifestacao(conn):
    codigo = int(input("Digite o codigo da maniofestação a ser removida: "))

    consulta = 'delete from manifestacoes where codigo = %s'
    valores = [codigo]

    manifestacaoRemovida = excluirBancoDados(conn, consulta, valores)

    if manifestacaoRemovida >= 1:
        print("A manifestação foi removida com sucesso!")

    else:
        print("O codigo informado é invalido.")

def quantidadeManifestacao(conn):

    consulta = "select count(*) from manifestacoes"
    manifestacoes = listarBancoDados(conn, consulta)

    print(manifestacoes[0][0], "Manifestações")