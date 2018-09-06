import hashlib
import modules.convertdcm as convert
import modules.loaddcm as load
import modules.cassandra.storecassandra as cassandra
import modules.hbase.storehbase as hbase
import modules.couchdb.storecouch as couch

## Input para receber arquivo dicom
while True:
        try:
                dcmfile = input('\n Digite o nome do arquivo a ser inserido (ex.: /home/unisul/dcmfiles/00000.dcm): ')
                open(dcmfile, "rb").readlines()
                break
        except FileNotFoundError:
                print('\n Arquivo não encontrado! Tente novamente... \n')

## Gera hash sha1 para o conteudo do arquivo
hashdcm = hashlib.sha1((dcmfile).encode('utf-8')).hexdigest()
print ('\n Hash gerado: ', hashdcm, '\n')

## Verifica se arquivo já foi inserido no Cassandra
cassandra.hasrow(hashdcm)

## Verifica se o arquivo já foi inserido no HBase
hbase.hasRow(hashdcm)

## Realiza a compressão do arquivo dcm e converte para a base64
encoded = convert.dcmtobase64(dcmfile)

## Retorna objeto contendo algumas tags do arquivo dcm
dcm = load.getobject(hashdcm, dcmfile)

## Insere arquivo dcm no hbase
hbase.store(encoded, hashdcm)

## Insere dados no couchdb
couch.store(dcm, hashdcm)

## Inserir arquivo dcm no Cassandra
cassandra.insert(hashdcm, dcm, encoded)