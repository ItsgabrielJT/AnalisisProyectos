import pandas as pd
import sqlite3 as sql


def createDB():
    conn = sql.connect("Datos.db") 
    conn.commit()
    conn.close()


def creteTableStreamers():
    conn = sql.connect("Datos.db")
    cursor = conn.cursor()
    cursor.execute(
         """CREATE TABLE streamers ( 
            id integer,
            channel text,
            watchtime integer,
            streamtime integer,
            Peakviewers integer,
            Averageviewers integer,
            Followers integer,
            Followersgained integer,
            Viewsgained integer,
            Partnered integer,
            Mature text,
            Language text
        )"""
    )   
    conn.commit()
    conn.close()

def creteTableVentas():
    conn = sql.connect("Datos.db")
    cursor = conn.cursor()
    cursor.execute(
         """CREATE TABLE ventas ( 
            id integer,
            link text,
            title text,
            rating text,
            price integer
        )"""
    )   
    conn.commit()
    conn.close()

def creteTableMillonarios():
    conn = sql.connect("Datos.db")
    cursor = conn.cursor()
    cursor.execute(
         """CREATE TABLE billonarios ( 
            id integer,
            name text,
            rank integer,
            year integer,
            companyfounded integer,
            companyname text,
            companyrelationship text,
            companysector text,
            companytype text,
            demographicsage integer,
            demographicsgender text,
            locationcitizenship text,
            locationcountrycode text,
            locationregion text,
            wealthtype text,
            wealthworthbillions text,
            wealthhowcategory text,
            wealthhowfromemerging text,
            wealthhowindustry text,
            wealthhowinherited text,
            wealthhowwasfounder text,
            wealthhowwaspolitical text
        )"""
    )   
    conn.commit()
    conn.close()

def introducir_streamers(url):
    datos = pd.read_csv(url)
    conn = sql.connect("Datos.db")
    cursor = conn.cursor()
    for fila in datos.itertuples():
        cursor.execute("INSERT INTO streamers (id, channel, watchtime,streamtime,Peakviewers,Averageviewers,Followers,Followersgained,Viewsgained,Partnered,Mature,Language) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12]))
        conn.commit()
    conn.close()

def introducir_ventas(url):
    datos = pd.read_csv(url)
    conn = sql.connect("Datos.db")
    cursor = conn.cursor()
    for fila in datos.itertuples():
        cursor.execute("INSERT INTO ventas (id, link, title, rating, price) VALUES (?, ?, ?, ?, ?)", (fila[1], fila[2], fila[3], fila[4], fila[5]))
        conn.commit()
    conn.close()

def introducir_billonarios(url):
    datos = pd.read_csv(url)
    conn = sql.connect("Datos.db")
    cursor = conn.cursor()
    for fila in datos.itertuples():
        cursor.execute("INSERT INTO billonarios (id,name,rank,year,companyfounded,companyname,companyrelationship,companysector,companytype,demographicsage,demographicsgender,locationcitizenship,locationcountrycode,locationregion,wealthtype,wealthworthbillions,wealthhowcategory,wealthhowfromemerging,wealthhowindustry,wealthhowinherited,wealthhowwasfounder,wealthhowwaspolitical) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12], fila[13], fila[14], fila[15], fila[16], fila[17], fila[18], fila[19], fila[20], fila[21], fila[22]))
        conn.commit()
    conn.close()

