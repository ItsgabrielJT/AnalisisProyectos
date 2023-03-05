from pymongo import MongoClient
import mysql.connector
import pandas as pd
import couchdb
import sqlite3

cliente_mongo = MongoClient('mongodb://localhost:27017/')
base_de_datos_mongo = cliente_mongo['datos_finales']

def insertar_sqliteStreamers_to_mongo(data):
    coleccion_mongo = base_de_datos_mongo['streamers']        
    sqlite_conexion = sqlite3.connect(data)
    sqlite_cursor = sqlite_conexion.cursor()
    sqlite_cursor.execute('SELECT * FROM streamers')
    resultados = sqlite_cursor.fetchall()
    for resultado in resultados:
        documento = {'id':resultado[0], 'channel':resultado[1], 'watchtime':resultado[2],'streamtime':resultado[3],'Peakviewers':resultado[4],'Averageviewers':resultado[5],'Followers':resultado[6],'Followersgained':resultado[7],'Viewsgained':resultado[8],'Partnered':resultado[9],'Mature':resultado[10],'Language':resultado[11] }
        coleccion_mongo.insert_one(documento)
    sqlite_conexion.close()

def insertar_sqliteVentas_to_mongo(data):
    coleccion_mongo = base_de_datos_mongo['ventas']        
    sqlite_conexion = sqlite3.connect(data)
    sqlite_cursor = sqlite_conexion.cursor()
    sqlite_cursor.execute('SELECT * FROM ventas')
    resultados = sqlite_cursor.fetchall()
    for resultado in resultados:
        documento = {'id':resultado[0], 'link':resultado[1], 'title':resultado[2],'rating':resultado[3],'price':resultado[4]}
        coleccion_mongo.insert_one(documento)
    sqlite_conexion.close()

def insertar_sqliteBillonarios_to_mongo(data):
    coleccion_mongo = base_de_datos_mongo['billonarios']        
    sqlite_conexion = sqlite3.connect(data)
    sqlite_cursor = sqlite_conexion.cursor()
    sqlite_cursor.execute('SELECT * FROM billonarios')
    resultados = sqlite_cursor.fetchall()
    for resultado in resultados:
        documento = {'id':resultado[0],'name':resultado[1],'rank':resultado[2],'year':resultado[3],'companyfounded':resultado[4],'companyname':resultado[5],'companyrelationship':resultado[6],'companysector':resultado[7],'companytype':resultado[8],'demographicsage':resultado[9],'demographicsgender':resultado[10],'locationcitizenship':resultado[11],'locationcountrycode':resultado[12],'locationregion':resultado[13],'wealthtype':resultado[14],'wealthworthbillions':resultado[15],'wealthhowcategory':resultado[16],'wealthhowfromemerging':resultado[17],'wealthhowindustry':resultado[18],'wealthhowinherited':resultado[19],'wealthhowwasfounder':resultado[20],'wealthhowwaspolitical':resultado[21]}
        coleccion_mongo.insert_one(documento)
    sqlite_conexion.close()
     

def insertar_couchdb_to_mongo():
    coleccion_mongo = base_de_datos_mongo['covid']
    servidor_couchdb = couchdb.Server('http://root:toor@localhost:5984/')
    base_de_datos_couch = servidor_couchdb['covid']
    for id in base_de_datos_couch:
        documento = base_de_datos_couch[id]
        coleccion_mongo.insert_one(documento)


def insertar_mysql_to_mongo():    
    coleccion_mongo = base_de_datos_mongo['spotify']
    conexion = mysql.connector.connect(host='127.0.0.1', user='root', password='toor', database='spotify')
    cursor = conexion.cursor()
    datos_mysql = []
    cursor.execute('SELECT * FROM musicas;')
    for fila in cursor:
        datos_mysql.append({'Id': fila[0], 'Name': fila[1], 'Artists': fila[2], 'Album':fila[3],'Release_Date': fila[4]})

    for registro in datos_mysql:
        coleccion_mongo.insert_one(registro)
    cursor.close()
    conexion.close()


def ejecutar_importaciones(data):
    insertar_couchdb_to_mongo()
    insertar_mysql_to_mongo()
    insertar_sqliteBillonarios_to_mongo(data)
    insertar_sqliteStreamers_to_mongo(data)
    insertar_sqliteVentas_to_mongo(data)
    cliente_mongo.close()




