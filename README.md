Script para inserção de arquivos dicom no HBase/CouchDB/Cassandra

Para funcionamento correto do script certifique-se que as seguintes bibliotecas estejam instaladas:
              - happybase
              - couchdb
              - cassandra-driver
              - base64
              - pydicom
              - sys
              - hashlib
Obs: Recomenda-se a criação de um ambiente virtual para instalação das bibliotecas acima (por exemplo, virtualenv)

Importante: 
            - Deve ser executado thrift server do HBase, antes de executar o script
              $ ./hbase-daemon.sh start thrift

            - Deve existir um keyspace de nome app criado no Cassandra

            CREATE KEYSPACE app
                WITH REPLICATION = {
                'class' : 'SimpleStrategy',
                'replication_factor' : 1
            };

            - Da mesma forma, deve existir uma tabela de nome app criada no Cassandra

            CREATE TABLE app (  
            id varchar primary key,
            patientid varchar,
            patientname varchar,
            examid varchar,
            serieid varchar,
            imageid varchar,
            modality varchar,
            studydate varchar,
            bodypart varchar,
            file
            );

Script compativel com a versão 3.x do Python

Comando para iniciar a aplicação:
              $ python3 app.py
