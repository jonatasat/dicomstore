import happybase as hbase
import sys

def connect():
        try:
                host = 'localhost'
                port = 9090
                conn = hbase.Connection(host,port)
                conn.open()
                return conn
        except:
                print('\n Não foi possível estabelecer a conexão com HBase! \n')
                sys.exit('\n Fechando a aplicação...')


def store(dcmencodedstring, hashdcm):
        conn = connect()
        try:
                table = conn.table('app')
                table.put(hashdcm, {'files:filesb64': dcmencodedstring})
        except:
                print('\n Não foi possível inserir o arquivo no HBase! \n')
                sys.exit('\n Fechando a aplicação...')

        print('Arquivo ', hashdcm,' armazenado no HBase.', '\n')

def hasRow(hashdcm):
        conn = connect()
        try:
                table = conn.table('app')
                rowreturned = table.row(hashdcm)
        except:
                print('\n Falha ao realizar pesquisa no HBase')
                sys.exit('\n Fechando a aplicação...')

        if rowreturned:
                print('Existe arquivo na base')
                sys.exit('\n Fechando a aplicação...')
