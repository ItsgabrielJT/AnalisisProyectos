import couchdb
import csv


def introducir_csv(url):
    server=couchdb.Server("http://root:toor@localhost:5984/")
    db=server['covid']

    datos = list()

    with open(url, newline='') as archivo:
        lector_csv = csv.reader(archivo)
        datos = list(lector_csv)

    for fila in datos:
        doc = {'ID':fila[0],'Unnamed: 0':fila[1],'#':fila[2],"Country, Other":fila[3],'Total Cases':fila[4],'Total Deaths':fila[5],'Total Recovered':fila[6],'Active Cases':fila[7],'Serious':fila[8], 'Critical':fila[9],'Tot Cases/ 1M pop':fila[10],'Deaths/ 1M pop':fila[11],'Total Tests':fila[12],'Tests/ 1M pop':fila[13],'Population':fila[13],'Continent':fila[14],'1 Case every X ppl':fila[15],'1 Death every X ppl':fila[16],'1 Test every X ppl':fila[17],'New Cases/1M pop':fila[18]}
        db.save(doc)