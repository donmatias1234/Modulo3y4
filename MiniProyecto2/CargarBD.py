import mysql.connector as db
import csv
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "dino1994",
    database = "Cine"
)

miCursor = mydb.cursor()

'''
with open('data/actors.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), row[1], row[2]]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python

sqlSentenceActors = 'INSERT INTO actors(id, first_name, last_name) VALUES (%s, %s, %s)'
miCursor.executemany(sqlSentenceActors, filas)
mydb.commit()
'''
#############################################################
'''
with open('data/directors.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), row[1], row[2]]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python

sqlSentenceDirectors = 'INSERT INTO directors(id, first_name, last_name) VALUES (%s, %s, %s)'
miCursor.executemany(sqlSentenceDirectors, filas)
mydb.commit()
'''

###################################################################################################################
#en cargar movies se hizo a y a traves de my (crando la table y cargando los datos directamnete ahi
# debido a un error en la conversion de valores NULL a float, de todas formas se deja el codigo que debiese importar el archivo csv a continuacion
###################################################################################################################
'''
with open('data/movies.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), row[1], int(row[2]), float(row[3])]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python

sqlSentenceMovies = 'INSERT INTO movies(id, name, year, ´rank´) VALUES (%s, %s, %s, %s)'
miCursor.executemany(sqlSentenceMovies, filas)
mydb.commit()
'''
#####################################################################################################
'''
with open('data/movies_actors.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), int(row[1]), row[2]]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python

sqlSentenceMoviesActors = 'INSERT INTO movies_actors(actor_id, movie_id, role) VALUES (%s, %s, %s)'
miCursor.executemany(sqlSentenceMoviesActors, filas)
mydb.commit()
'''

##################################################################################################
'''
with open('data/movies_directors.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), int(row[1])]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python

sqlSentenceMoviesDirectors = 'INSERT INTO movies_directors(director_id, movie_id) VALUES (%s, %s)'
miCursor.executemany(sqlSentenceMoviesDirectors, filas)
mydb.commit()
'''