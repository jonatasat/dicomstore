import sys
from cassandra.cluster import Cluster


def connect():
        try:
                cluster = Cluster(['localhost'])
                session = cluster.connect('app')
                return session
        except:
                print("\n Falha ao conectar no Cassandra!")
                sys.exit('\n Fechando a aplicação...')

def insert(hashdcm, objdcm, dcmfile):
        try:
                session = connect()
                patientid = str(objdcm.patientid)
                patientname = str(objdcm.patientname)
                examid = str(objdcm.examid)
                serieid = str(objdcm.serieid)
                imageid = str(objdcm.imageid)
                modality = str(objdcm.modality)
                studydate = objdcm.studydate
                bodypart = str(objdcm.bodypart)
                session.execute("INSERT INTO APP(id, patientid, patientname, examid, serieid, imageid, modality, studydate, bodypart, file) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (hashdcm, patientid, patientname, examid, serieid, imageid, modality, studydate, bodypart, dcmfile))
                print("\n Arquivo "+hashdcm+" inserido no Cassandra!")
        except:
                print("\n Falha ao inserir no Cassandra!")
                sys.exit('\n Fechando a aplicação...')

def hasrow(hashdcm):
        try:
                session = connect()
                rows = session.execute("SELECT id FROM APP")
        except:
                print("\n Falha ao realizar pesquisa no Cassandra!")
                sys.exit('\n Fechando a aplicação...')

        for row in rows:
                if str(hashdcm) == row.id:
                        print('\n Existe arquivo na base!')
                        sys.exit('\n Fechando a aplicação...')
