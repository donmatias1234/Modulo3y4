import csv

import mysql.connector as db

mydb = db.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dino1994',
    database = 'taller1'
)


###################################################
#miCursor = mydb.cursor()
##aqui cree la tabla, solo tengo que hacerlo y ocupar commit una vez (ya esta creada)
#sqlCrearTabla= 'CREATE TABLE comunas2(cod_comuna INTEGER PRIMARY KEY, nombre VARCHAR(45), telefono VARCHAR(45))'
#miCursor.execute(sqlCrearTabla)
#mydb.commit()
######################################################

with open('data/comunas2.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), row[1], row[2]]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python



miCursor = mydb.cursor()
sqlSentence = 'INSERT INTO comunas2(cod_comuna, nombre, telefono) VALUES (%s, %s, %s)'
miCursor.executemany(sqlSentence, filas)
mydb.commit()