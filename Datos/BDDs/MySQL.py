import mysql.connector
import pandas as pd

conexion = mysql.connector.connect(host='127.0.0.1', user='root', password='toor', database='spotify')
cursor = conexion.cursor()

def introducir_mysql(url):
    datos = pd.read_csv(url)
    
    for fila in datos.itertuples():
        cursor.execute("INSERT INTO musicas (Name, Artists, Album, Release_Date) VALUES (%s, %s, %s, %s)", (fila[2], fila[3], fila[4], fila[5]))
        conexion.commit()

    cursor.close()
    conexion.close()
