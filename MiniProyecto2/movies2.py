import mysql.connector as db
import csv
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "dino1994",
    database = "Cine"
)

miCursor = mydb.cursor()

#sqlCrearMovies2= 'CREATE TABLE movies2(id INT PRIMARY KEY, name VARCHAR(50), year INT, `rank` FLOAT)'
#miCursor.execute(sqlCrearMovies2)

with open('data/movies2.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), row[1], int(row[2]), float(row[3])]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python

sqlSentenceMovies2 = 'INSERT INTO movies2(id, name, year, ´rank´) VALUES (%s, %s, %s, %s)'
miCursor.executemany(sqlSentenceMovies2, filas)
#mydb.commit()