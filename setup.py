from setuptools import setup

setup(name='dicomstore',
        version='0.1',
        description='Inserção de dados de arquivos dicom nos bancos de dados: HBase, CouchDB e Cassandra',
        url='http://github.com/jonatasat/dicomstore',
        author='Jonatas Tavares',
        author_email='jonatasatavares@gmail.com',
        license='MIT',
        packages=['app', 'cassandra', 'couchdb', 'hbase'],
        zip_safe=False)