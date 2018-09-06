import couchdb
import sys
import json

table = 'app'

def connect():
        try:
                return couchdb.Server('http://localhost:5984/')
        except:
                print('\n Não foi possível realizar a conexão com o CouchDB')
                sys.exit('\n Fechando a aplicação...')

def store(objdcm, hashdcm):
        couch = connect()

        try:
                db = couch[table]
        except:
                print('\n Tabela', table, 'não encontrada no CouchDB')
                sys.exit('\n Fechando a aplicação...')

        patientid = str(objdcm.patientid)
        patientname = str(objdcm.patientname)
        examid = str(objdcm.examid)
        serieid = str(objdcm.serieid)
        imageid = str(objdcm.imageid)
        modality = str(objdcm.modality)
        studydate = objdcm.studydate
        bodypart = str(objdcm.bodypart)


        doc = {'id_doc': hashdcm, 'patient_name': patientname, 'patient_id': patientid, 'study_date': studydate, 'modality': modality, 'examid': examid, 'serieid': serieid, 'imageid': imageid, 'bodypart': bodypart}

        try:
                save = db.save(doc)
                print('\n Arquivo '+ hashdcm + ' armazenado no banco CouchDB \n')
                return save
        except:
                print('\n Falha ao inserir dados no banco CouchDB')
                sys.exit('\n Fechando a aplicação...')
