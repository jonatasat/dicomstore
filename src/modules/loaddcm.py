import pydicom
import sys

def getobject(hashdcm, dcmfile):
        class DcmObj:
                def __init__(self, hashid,  patientname, patientid, examid, serieid, imageid, modality, studydate, bodypart):
                        self.hashid = hashid
                        self.patientname = patientname
                        self.patientid = patientid
                        self.examid = examid
                        self.serieid = serieid
                        self.imageid = imageid
                        self.modality = modality
                        self.studydate = studydate
                        self.bodypart = bodypart

        try:
                ds = pydicom.dcmread(dcmfile)
                DcmObj.hashid = hashdcm
                if (0x0010, 0x0010) in ds:
                        DcmObj.patientname = ds[0x0010, 0x0010].value
                else:
                        DcmObj.patientname = ""
                if (0x0010, 0x0020) in ds:
                        DcmObj.patientid = ds[0x0010, 0x0020].value
                else:
                        DcmObj.patientid = ""
                if (0x0008, 0x0018) in ds:
                        DcmObj.examid = ds[0x0008, 0x0018].value
                else:
                        DcmObj.examid = ""
                if (0x0020, 0x000e) in ds:
                        DcmObj.serieid = ds[0x0020, 0x000e].value
                else:
                        DcmObj.serieid = ""
                if (0x0020, 0x000d) in ds:
                        DcmObj.imageid = ds[0x0020, 0x000d].value
                else:
                        DcmObj.imageid = ""
                if (0x0008, 0x0020) in ds:
                        DcmObj.studydate = ds[0x0008, 0x0020].value
                else:
                        DcmObj.studydate = ""
                if (0x0008, 0x0060) in ds:
                        DcmObj.modality = ds[0x0008, 0x0060].value
                else:
                        DcmObj.modality = ""
                if (0x0018, 0x0015) in ds:
                        DcmObj.bodypart = ds[0x0018, 0x0015].value
                else:
                        DcmObj.bodypart = ""
        
                return DcmObj
        except IOError:
                print('\n Falha ao abrir o arquivo dcm')
                sys.exit('\n Fechando aplicação...')
        except:
                print('\n Falha ao ler o arquivo dicom')
                sys.exit('\n Fechando a aplicação...')