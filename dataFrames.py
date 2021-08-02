import pandas as pd

import mysql.connector as db
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "Energia"
)


#Leyendo un archivo directamente desde un dataframe
#df1 = pd.read_csv('data/personas3.csv', sep = ';')
#df2 = df1[[ 'rut', 'nombre','fecha_nac']]

#print(df1)
#print(df2)

#Slicing del dataframe
#print(df2.iloc[0:4,0:1])
#print(df2.loc[5:7,['rut', 'nombre']])
'''
#Leyendo el resultado desde mysql y ponindo el resultado en un Dataframe
miCursor = mydb.cursor()
sqlSentence = 'SELECT * FROM Consumos WHERE consumos.consumo > 800 and consumos.consumo < 900'
miCursor.execute(sqlSentence)
#lo que obtenmos de la BD
rows = miCursor.fetchall()
#vamos a generar una lista con el resultado de esta consulta, para ello hacemos un loop con row(iterador) in rows (lista, que en el for funciona como largo de la lista)
lista =[]
for row in rows:
#con la instrucción de abajo vamos a ir llenando la lista, fila por fila
  lista.append(row)
df3 = pd.DataFrame(lista, columns=['id', 'Año', 'Tipo', 'Actividad', 'SubActividad', 'Cod_region','Consumo'])
#print(df3.loc[:, ['Año','Tipo', 'Cod_region', 'Consumo']])


#aca estoy mostrando los valores del dataframe df3 pero convertidos en una lista
print(df3.values.tolist())
#Aca convertire cada minilista de la lista grande en una tupla,
#por eso "l" recorre los valores de la lista df3.values.tolist(), los elementos que la componene son minilistas
#que las queremos en tuplas, la lista de tuplas se puede pasar como paramentro al insert
tuple_list = [tuple(l) for l in df3.values.tolist()]

#eliminamos contenido de tabla Consumos
miCursor.execute('DELETE FROM Consumos')
#lo siguiente hace que la ejecución se aplique en la BD que está en mysql
mydb.commit()

sqlSentence ='INSERT INTO Consumos(id, Año, Tipo, Actividad, SubActividad, Cod_region, Consumo) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)'
miCursor.executemany(sqlSentence,tuple_list)
mydb.commit()

'''
