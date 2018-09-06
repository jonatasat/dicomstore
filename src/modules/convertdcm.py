import base64
import sys
import zlib

def dcmtobase64(dcm):
        try:
                dcmfileread = open(dcm, "rb").read()
                dcmfileencoded = zlib.compress(base64.encodestring(dcmfileread))
                print('\n Arquivo .dcm convertido para base 64.', '\n')
                return dcmfileencoded
        except IOError:
                print('\n Falha ao abrir o arquivo dcm')
                sys.exit('\n Fechando aplicação...')
        except:
                print('\n Falha ao converter o arquivo para base64.')
                sys.exit('\n Fechando aplicação...')