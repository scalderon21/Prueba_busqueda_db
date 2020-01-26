import mysql.connector
import sys
import pandas as pd
from BD import Connection

df = pd.read_excel('C:/Users/sebai/source/repos/Prueba_busqueda_db/Prueba_busqueda_db/test.xlsx',index = False)

db_config =  {
            'host':"localhost",                 # database host
            'port': 3306,                       # port
            'user':"root",                      # username
            'passwd':"",                   # password
            'db':"db_prueba"
            }


sql = "SELECT idDocumento,comentario FROM db_prueba.comentario" 
con = Connection.Connection(db_config)
cursor = con.get_rows(sql)

def definir_banco(comentario):
    banco = ""

    return banco


for (idDocBD,comentario) in cursor:
    for idDocExcel in df['id_documento']:
        if(idDocBD == idDocExcel):
            print(comentario)