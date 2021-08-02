import csv
import mysql.connector as db
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "Energia"
)
miCursor = mydb.cursor()
#Leyendo un archivo directamente desde un dataframe
#df1 = pd.read_csv('data/Energia_consumos2.csv', sep = ';')
#print(df1)

#sqlCrearTabla= 'CREATE TABLE consumos2(id INTEGER PRIMARY KEY, age INTEGER, type VARCHAR(45), activity VARCHAR(45),  \
#               subactivity VARCHAR(45), region INTEGER, tcal DOUBLE)'
#miCursor.execute(sqlCrearTabla)
'''
####################### Poblar la tabla #################################
with open('data/Energia_consumos2.csv') as csvfile:  #se abre el archivo csv y se asigna al objeto csvfile
    readCSV = csv.reader(csvfile, delimiter=';')  #se lee el archivo csvfile y le digo que se delimita con ;
    filas= []                                      #creo una lista
    first = next(readCSV)                           #me salto los encabezados con el next
    for row in readCSV:                             #row recorre todos los elementos del readcsv
        print('Fila a agregar: ')
        print(row)
        filas.append(tuple([int(row[0]), int(row[1]), row[2], row[3], row[4], int(row[5]), float(row[5])]))  #append agrega al final de la lista, convertimos lo que viene como lista del archivo
                                                            # row[0]), row[1], row[2] en una tupla python
miCursor = mydb.cursor()
sqlSentence = 'INSERT INTO consumos2(id, age, type, activity, subactivity, region, tcal) VALUES (%s, %s, %s, %s, %s, %s, %s)'
miCursor.executemany(sqlSentence, filas)
mydb.commit()
'''
############################################################
#sqlSentence='SELECT * FROM consumos2'
#sqlSentence= 'SELECT type, SUM(tcal) FROM consumos2 GROUP BY type'
#sqlSentence= 'SELECT type, SUM(tcal) FROM consumos2 GROUP BY type ORDER BY SUM(tcal) DESC' # ORDER BY descendente o ascendente tiene que ser por un valor nrumerico
#sqlSentence= 'SELECT type, SUM(tcal) AS total FROM consumos2 GROUP BY type HAVING total>3000 ORDER BY SUM(tcal) DESC'
sqlSentence= 'SELECT type, SUM(tcal) AS total FROM consumos2 \
             WHERE age>2015 \
             GROUP BY type HAVING total>3000 ORDER BY SUM(tcal) ASC'
miCursor.execute(sqlSentence)
rows = miCursor.fetchall()
for row in rows:
    print(row)

#mydb.commit()
